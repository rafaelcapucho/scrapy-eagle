import os
import signal
from datetime import datetime, timedelta

import gevent


def heartbeat_servers(redis_conn, ip, hostname):

    while True:

        future = datetime.now() + timedelta(seconds=6)

        redis_conn.zadd(
            'eagle_servers',
            '{ip}-{hostname}'.format(ip=ip, hostname=hostname),
            int(future.timestamp())
        )

        # now = datetime.now()
        # servers = redis_conn.zrangebyscore('servers', now.timestamp(), max='+inf')

        gevent.sleep(3)


def heartbeat_subprocess(pid, spider, max_seconds_idle, max_size_limit, queue_info_global):

    last_processed = None

    max_size = 0

    while True:

        size = None
        for entry in queue_info_global:
            if entry['name'] == spider:
                size = entry['size']

        if size > 0:
            last_processed = datetime.now()

        if size > max_size:
            max_size = size

        if last_processed:
            diff = datetime.now() - last_processed

            # print('\nlast_processed_secs: ', diff.seconds, ' maxsize: ', max_size, ' size: ', size, '\n\n')

            if diff.seconds > max_seconds_idle and max_size > max_size_limit:

                os.kill(pid, signal.SIGHUP)

                break

        gevent.sleep(2)
