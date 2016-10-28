from gevent import monkey
monkey.patch_all()

import gevent
import gevent.pool

from scrapy_eagle.dashboard import settings
from scrapy_eagle.dashboard.utils.processkit import get_resources_info_from_pid, get_resources_info_from_server

def send_redis_queue_info(socketio, redis_conn, spiders, queue_info_global):

    while True:

        queues = []

        for spider in spiders:
            queues.append(
                {
                    'name': spider,
                    'size': int(redis_conn.llen('{spider}:requests'.format(spider=spider)))
                }
            )

        # Don't asign directly to maintain the reference to the global object
        queue_info_global.clear()
        queue_info_global.extend(queues)

        socketio.emit('redis_queue_info', {'data': queues}, namespace="/queues", broadcast=True)

        gevent.sleep(1)

def send_resources_info(socketio, subprocess_pids, public_ip):

    while True:

        dict_info_pid_greenlet = gevent.spawn(get_resources_info_from_pid)
        dict_info_host_greenlet = gevent.spawn(get_resources_info_from_server)

        subprocess_info_greenlets = []

        for pid, spider, command, base_dir, created_at in subprocess_pids:

            # We pass all the parameters that we like to keep instead
            # of simply use a .update() here because the returned instance
            # is a Greenlet instead of a dict.

            info_greenlet = gevent.spawn(
                get_resources_info_from_pid,
                pid=pid,
                spider=spider,
                command=command,
                base_dir=base_dir,
                created_at=created_at,
            )

            subprocess_info_greenlets.append(info_greenlet)

        dict_info_pid_greenlet.join()
        dict_info = dict_info_pid_greenlet.get()
        dict_info['public_ip'] = public_ip

        dict_info_host_greenlet.join()
        dict_info_host = dict_info_host_greenlet.get()
        dict_info.update(dict_info_host)

        gevent.joinall(subprocess_info_greenlets)
        dict_info['sub'] = [greenlet.get() for greenlet in subprocess_info_greenlets]

        # When get_resources_info try to access a PID that dont exists any more it
        # return None, here we remove those results. It happen because it takes
        # sometime to subprocess_pids remove PIDs that finishs.
        dict_info['sub'] = [x for x in dict_info['sub'] if x]

        _spiders = settings.get_spiders()
        _commands = settings.get_commands()

        dict_info['spiders'] = _spiders or []
        dict_info['commands'] = _commands or []

        print('\n\ndict_info: ', dict_info, '\n\n')

        socketio.emit('resources_info', {'data': dict_info}, namespace="/resources", broadcast=True)

        gevent.sleep(1)