import subprocess

from scrapy_eagle.dashboard import settings


def find_spiders():

    _config = settings.get_config_file()

    base_dir = _config.get('scrapy', 'base_dir')
    binary = _config.get('scrapy', 'binary')

    spiders = []

    with subprocess.Popen(
            [binary, 'list'],
            cwd=base_dir,
            stdout=subprocess.PIPE,
            bufsize=1,
            universal_newlines=True
    ) as p:
        for line in p.stdout:
            spiders.append(line.strip())

    return spiders
