import argparse

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

from scrapy_eagle.dashboard.utils import ip

# Never import these directly
# Use get_config and get_args instead
_args = None
_config = None
_public_ip = None
_hostname = None

def setup():

    global _args, _config, _public_ip, _hostname

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-c', '--config-file', help='Config file path.')

    _args = parser.parse_args()

    if not _args.config_file:
        print('You should specify a config file using --config-file parameter.')
        exit(0)

    _config = configparser.ConfigParser()
    _config.read(_args.config_file)

    globals()['config'] = _config

    print('discovering your external entrypoint address... ', end='', flush=True)

    _public_ip = ip.get_external_ip()

    print(_public_ip)

    _hostname = ip.get_hostname()

    return _args, _config

def get_public_ip():
    return _public_ip

def get_hostname():
    return _hostname

def get_config():
    return _config

def get_args():
    return _args