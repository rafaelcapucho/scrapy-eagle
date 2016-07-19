import argparse

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

# Never import these directly
# Use get_config and get_args instead
args = None
config = None

def setup():

    global args, config

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-c', '--config-file', help='Config file path.')

    args = parser.parse_args()

    if not args.config_file:
        print('You should specify a config file using --config-file parameter.')
        exit(0)

    config = configparser.ConfigParser()
    config.read(args.config_file)

    globals()['config'] = config

    return args, config

def get_config():
    return config

def get_args():
    return args