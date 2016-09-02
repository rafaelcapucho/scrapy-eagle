import os

from scrapy_eagle.dashboard import settings


def load_commands_name(dir):

    if os.path.exists(dir):

        module_names = []

        for d in os.listdir(dir):
            if d.find("__init__") == -1 and d.endswith('.py'):

                # Remove possible spaces
                d = d.replace(" ", "")

                # Remove the Extension
                d = ".".join(d.split(".")[:-1])

                module_names.append(d)

        module_names.sort()

        return module_names

    else:
        return []


def find_commands():

    _config = settings.get_config_file()

    base_dir = _config.get('commands', 'base_dir')

    return load_commands_name(dir=base_dir)
