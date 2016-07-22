import gevent

from scrapy_eagle.dashboard import settings
from scrapy_eagle.dashboard.utils import spiderskit

def find_new_spiders():

    while True:

        # Open the process and execute Scrapy's list command
        _spiders = spiderskit.find_spiders()

        # Install the list of spiders names
        settings._spiders = _spiders

        gevent.sleep(10)