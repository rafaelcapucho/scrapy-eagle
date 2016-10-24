import gevent
from datetime import datetime

from scrapy_eagle.dashboard import settings
from scrapy_eagle.dashboard.memory import get_job_object, update_job_object

from scrapy_eagle.dashboard.utils import iso_to_timestamp, timestamp_to_utc


def dispatch(redis_conn):

    while True:

        _spiders = settings.get_spiders()
        _commands = settings.get_commands()

        # When the system is starting up, spiders/commands may return empty because
        # we're using async execution `green_threads.find_new_spiders`.
        if _spiders and _commands:

            for key in _spiders + _commands:
                obj = get_job_object(key=key)

                if obj and obj.get('last_started_at'):

                    last = timestamp_to_utc(iso_to_timestamp(obj['last_started_at']))

                    now = datetime.utcnow()

                    print(now - last)

        gevent.sleep(3)
