import os
import signal
from datetime import datetime, timezone, timedelta

import gevent

def heartbeat_servers(redis_conn, ip, hostname):

    while True:

        future = datetime.now() + timedelta(seconds=6)

        redis_conn.zadd(
            'servers',
            '{ip}-{hostname}'.format(ip=ip, hostname=hostname),
            int(future.timestamp())
        )

        now = datetime.now()

        servers = redis_conn.zrangebyscore('servers', now.timestamp(), max='+inf')

        gevent.sleep(3)