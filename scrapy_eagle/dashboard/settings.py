import argparse

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

from scrapy_eagle.dashboard.utils import ip

buffers = {}

queue_info_global = []

subprocess_pids = set()

# Never import these directly
# Use get_config_file and get_args instead
_args = None
_config = None
_public_ip = None
_hostname = None
_spiders = None
_commands = None


def setup_configuration(config_file=None):

    global _config

    _config = configparser.RawConfigParser()
    _config.read(config_file)

    globals()['_config'] = _config

    return _config


def setup(config_file=None, output=True):

    global _args, _config, _public_ip, _hostname

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-c', '--config-file', help='Config file path.')

    _args = parser.parse_args()

    if not _args.config_file and not config_file:
        print('You should specify a config file using --config-file parameter.')
        exit(0)

    _config = setup_configuration(config_file=_args.config_file or config_file)

    if output:
        print('discovering your external entrypoint address... ', end='', flush=True)

    _public_ip = ip.get_external_ip()

    if output:
        print(_public_ip)

    _hostname = ip.get_hostname()

    return _args, _config


def get_public_ip():
    return _public_ip


def get_hostname():
    return _hostname


def get_config_file():
    return _config


def get_args():
    return _args


def get_spiders():
    return _spiders


def get_commands():
    return _commands