import gevent
from datetime import datetime, timedelta

from scrapy_eagle.dashboard import settings
from scrapy_eagle.dashboard.memory import get_job_object, update_job_object
from scrapy_eagle.dashboard.utils import iso_to_timestamp, timestamp_to_utc, processkit


def evaluation_loop():

    while True:

        _spiders = settings.get_spiders()
        _commands = settings.get_commands()

        # When the system is starting up, spiders/commands may return empty because
        # we're using async execution `green_threads.find_new_spiders`.
        if _spiders and _commands:

            for key in _spiders + _commands:
                obj = get_job_object(key=key)

                if obj and obj.get('next_execution_at'):

                    next_execution_at = timestamp_to_utc(iso_to_timestamp(obj['next_execution_at']))

                    now = datetime.utcnow()

                    if next_execution_at < now:

                        dispatch(key=key, register=obj)

        gevent.sleep(3)


def dispatch(key, register):

    _config = settings.get_config_file()

    register['last_started_at'] = datetime.utcnow().isoformat()
    register['next_execution_at'] = (datetime.utcnow() + timedelta(minutes=register['frequency_minutes'])).isoformat()

    if register['job_type'] == "spider":
        command = [_config.get('scrapy', 'binary'), 'crawl', key]
        base_dir = _config.get('scrapy', 'base_dir')
        spider = True

    elif register['job_type'] == "command":
        command = [_config.get('commands', 'binary'), '-u', key + '.py']
        base_dir = _config.get('commands', 'base_dir')
        spider = False

    gevent.spawn(
        processkit.new_subprocess,
        base_dir=base_dir,
        command=command,
        spider=spider,
        subprocess_pids=settings.subprocess_pids,
        queue_info_global=settings.queue_info_global,
        buffers=settings.buffers
    )

    update_job_object(key=key, fields=register)
