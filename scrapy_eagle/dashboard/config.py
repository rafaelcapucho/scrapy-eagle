import argparse

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

# Never import these directly
# Use get_config and get_args instead
_args = None
_config = None

def setup():

    global _args, _config

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-c', '--config-file', help='Config file path.')

    _args = parser.parse_args()

    if not _args.config_file:
        print('You should specify a config file using --config-file parameter.')
        exit(0)

    _config = configparser.ConfigParser()
    _config.read(_args.config_file)

    globals()['config'] = _config

    return _args, _config

def get_config():
    return _config

def get_args():
    return _args