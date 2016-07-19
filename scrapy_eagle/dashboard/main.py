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

from scrapy_eagle.dashboard.config import setup
from scrapy_eagle.dashboard.memory import get_connection


app = flask.Flask(__name__)

def main():

    # Install the arguments and config file inside the config module
    args, config = setup()

    print('discovering your external entrypoint address... ', end='', flush=True)

    public_ip = ip.get_external_ip()

    print(public_ip)

    hostname = ip.get_hostname()


@app.route('/')
def hello_world():
    return 'Hello World!'


def shutdown():

    print('\nshutting down {0}...'.format(threading.currentThread().getName()))

    sys.exit(0)


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

        # use_reloader: avoid Flask execute twice
        socketio.run(app, host='0.0.0.0', port=5001, use_reloader=False)

    except (KeyboardInterrupt, SystemExit):
        shutdown()


if __name__ == "__main__":

    entry_point()

