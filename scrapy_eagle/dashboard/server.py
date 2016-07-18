from gevent import monkey
monkey.patch_all()

import sys
import signal
import argparse
import threading

import redis
import flask
import gevent
from flask_cors import CORS
from flask_socketio import SocketIO, emit

from scrapy_eagle.dashboard.utils import ip

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'ha74%ahtus342'
app.config['DEBUG'] = True
CORS(app)

socketio = SocketIO(app, async_mode='gevent')

redis_pool, redis_conn = (None, None)


def main():

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-c', '--config-file', help='Config file path.')

    args = parser.parse_args()

    if not args.config_file:
        print('You should specify a config file using --config-file parameter.')
        exit(0)

    config = configparser.ConfigParser()
    config.read(args.config_file)

    print('discovering your external entrypoint address... ', end='', flush=True)

    public_ip = ip.get_external_ip()

    print(public_ip)

    hostname = ip.get_hostname()

    redis_pool = redis.ConnectionPool(
        host=config['redis']['host'],
        port=config['redis']['port'],
        db=config['redis']['db']
    )

    redis_conn = redis.Redis(connection_pool=redis_pool)

    print("Executing the server...")

@app.route('/')
def hello_world():
    return 'Hello World!'

def shutdown():

    print('\nshutting down {0}...'.format(threading.currentThread().getName()))

    sys.exit(0)

if __name__ == "__main__":

    # Graceful shutdown when kill are received
    signal.signal(signal.SIGTERM, lambda sig, frame: shutdown())

    # Graceful shutdown when terminal session are closed
    signal.signal(signal.SIGHUP, lambda sig, frame: shutdown())

    main()

    try:

        # use_reloader: avoid Flask execute twice
        socketio.run(app, host='0.0.0.0', port=5001, use_reloader=False)

    except (KeyboardInterrupt, SystemExit):
        shutdown()