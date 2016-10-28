from gevent import monkey
monkey.patch_all()

import os
import sys
import signal
import threading

import flask
import gevent

from flask_cors import CORS
from flask_socketio import SocketIO

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

from scrapy_eagle.dashboard import settings
from scrapy_eagle.dashboard import memory
from scrapy_eagle.dashboard.green_threads import heartbeat, stats, find_new_spiders, find_new_commands, executor
from scrapy_eagle.dashboard.utils import processkit


app = flask.Flask(__name__, static_folder='templates/static')


def main():

    # Install the arguments and config file inside the config module
    _, _ = settings.setup()


def shutdown():

    # Send a signal to all opened subprocess, closing them.
    for pid, _, _, _, _ in settings.subprocess_pids:

        print('killing subprocess: {pid}'.format(pid=pid))

        os.kill(pid, signal.SIGHUP)

    print('\nshutting down {0}...'.format(threading.currentThread().getName()))

    sys.exit(0)


def start_periodics(socketio):

    redis_conn = memory.get_connection()
    public_ip = settings.get_public_ip()
    hostname = settings.get_hostname()

    for i in range(3):
        gevent.spawn(
            processkit.new_subprocess,
            base_dir='.',
            subprocess_pids=settings.subprocess_pids,
            queue_info_global=settings.queue_info_global,
            buffers=settings.buffers
        )

    gevent.spawn(heartbeat.heartbeat_servers, redis_conn, public_ip, hostname)
    gevent.spawn(stats.send_resources_info, socketio, settings.subprocess_pids, public_ip)
    gevent.spawn(executor.evaluation_loop)
    gevent.spawn(find_new_spiders)
    gevent.spawn(find_new_commands)


def entry_point():

    # Graceful shutdown when kill are received
    signal.signal(signal.SIGTERM, lambda sig, frame: shutdown())

    # Graceful shutdown when terminal session are closed
    signal.signal(signal.SIGHUP, lambda sig, frame: shutdown())

    main()

    try:

        _config = settings.get_config_file()

        app.config['SECRET_KEY'] = _config.get('server', 'cookie_secret_key')
        app.config['DEBUG'] = _config.getboolean('server', 'debug', fallback=True)

        from scrapy_eagle.dashboard.views import servers, processes, root, jobs, react_app

        app.register_blueprint(root.root, url_prefix='/')
        app.register_blueprint(react_app.react_app, url_prefix='/app')
        app.register_blueprint(servers.servers, url_prefix='/servers')
        app.register_blueprint(processes.processes, url_prefix='/processes')
        app.register_blueprint(jobs.jobs, url_prefix='/jobs')

        CORS(app)

        socketio = SocketIO(app, async_mode='gevent')

        start_periodics(socketio)

        # use_reloader: avoid Flask execute twice
        socketio.run(
            app=app,
            host=_config.get('server', 'host', fallback='0.0.0.0'),
            port=_config.getint('server', 'port', fallback=5000),
            use_reloader=False
        )

    except (KeyboardInterrupt, SystemExit):

        shutdown()


if __name__ == "__main__":

    entry_point()
