from gevent import monkey
monkey.patch_all()

import sys
import signal
import threading

from datetime import datetime

import redis
import flask
import json
import gevent

from flask_cors import CORS
from flask_socketio import SocketIO, emit

from scrapy_eagle.dashboard.utils import ip

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

# from scrapy_eagle.dashboard.config import setup, get_hostname, get_public_ip
from scrapy_eagle.dashboard import config
from scrapy_eagle.dashboard import memory
from scrapy_eagle.dashboard.green_threads import heartbeat, stats


app = flask.Flask(__name__)

subprocess_pids = set()

def main():

    # Install the arguments and config file inside the config module
    _args, _config = config.setup()

    # gevent.spawn(heartbeat.heartbeat_servers, redis_conn, public_ip, hostname)
    # gevent.spawn(stats.send_resources_info, socketio, subprocess_pids, public_ip)


@app.route('/')
def hello_world():
    return 'Hello World!'


def shutdown():

    print('\nshutting down {0}...'.format(threading.currentThread().getName()))

    sys.exit(0)


def start_periodics(socketio):

    redis_conn = memory.get_connection()
    public_ip = config.get_public_ip()
    hostname = config.get_hostname()

    gevent.spawn(heartbeat.heartbeat_servers, redis_conn, public_ip, hostname)
    gevent.spawn(stats.send_resources_info, socketio, subprocess_pids, public_ip)

def entry_point():

    # Graceful shutdown when kill are received
    signal.signal(signal.SIGTERM, lambda sig, frame: shutdown())

    # Graceful shutdown when terminal session are closed
    signal.signal(signal.SIGHUP, lambda sig, frame: shutdown())

    main()

    try:

        print("Executing the server...")

        app.config['SECRET_KEY'] = 'ha74%ahtus342'
        app.config['DEBUG'] = True

        from scrapy_eagle.dashboard.views import servers

        app.register_blueprint(servers.servers, url_prefix='/servers')

        CORS(app)

        socketio = SocketIO(app, async_mode='gevent')

        start_periodics(socketio)

        # use_reloader: avoid Flask execute twice
        socketio.run(app, host='0.0.0.0', port=5001, use_reloader=False)

    except (KeyboardInterrupt, SystemExit):
        shutdown()


if __name__ == "__main__":

    entry_point()

