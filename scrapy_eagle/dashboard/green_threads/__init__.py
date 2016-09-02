import gevent

from scrapy_eagle.dashboard import settings
from scrapy_eagle.dashboard.utils import spiderskit, commandskit


def find_new_spiders():

    while True:

        # Open the process and execute Scrapy's list command
        _spiders = spiderskit.find_spiders()

        # Install the list of spiders names
        settings._spiders = _spiders

        gevent.sleep(10)


def find_new_commands():

    while True:

        # Monitoring the command folder
        _commands = commandskit.find_commands()

        # Install the list of commands names
        settings._commands = _commands

        gevent.sleep(5)