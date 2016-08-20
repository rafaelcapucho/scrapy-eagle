#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import subprocess
from datetime import datetime

import psutil
import gevent

from scrapy_eagle.dashboard.green_threads import heartbeat


def new_subprocess(base_dir, subprocess_pids, queue_info_global, command=None, spider=None, buffers={}):

    if not command:
        command = ['python', '-u', 'generator.py']
    # command = ['galculator']
    # command = ['/usr/bin/scrapy-py35', 'crawl', '{spider}'.format(spider)]

    with subprocess.Popen(
            command,
            cwd=base_dir,
            stdout=subprocess.PIPE,
            bufsize=1,
            universal_newlines=True
    ) as p:

        # Turn it JSON serializable
        created_at = datetime.utcnow().isoformat()

        identifier = (p.pid, spider, " ".join(command), base_dir, created_at)

        subprocess_pids.add(identifier)

        buffers[p.pid] = {'finished': False, 'lines': []}

        if spider:
            gevent.spawn(
                heartbeat.heartbeat_subprocess,
                p.pid,
                spider,
                max_seconds_idle=20,
                max_size_limit=15,
                queue_info_global=queue_info_global
            )

        for line in p.stdout:

            # TODO: remove empty lines

            if len(line.strip()) > 0:

                buffers[p.pid]['lines'].append(line)

            # print(line, end='', flush=True)

    buffers[p.pid]['finished'] = True

    subprocess_pids.remove(identifier)


def _get_info_from_pid(pid=None):

    if not pid:
        pid = os.getpid()

    process = psutil.Process(pid)

    mem = process.memory_info()[0] / float(2 ** 20)
    mem = float('{0:.2f}'.format(mem))

    cpu = process.cpu_percent(interval=0.5)

    return pid, mem, cpu


def get_resources_info_from_server():

    cpus = psutil.cpu_percent(interval=0.5, percpu=True)

    # Mem results return in bytes
    vmem = psutil.virtual_memory()

    total = vmem.total
    total = (total / 1024.0) / 1024.0

    available = vmem.available
    available = (available / 1024.0) / 1024.0

    used = total - available

    return {
        'cpus': cpus,
        'memory_total_mb': float('{0:.2f}'.format(total)),
        'memory_available_mb': float('{0:.2f}'.format(available)),
        'memory_used_server_mb': float('{0:.2f}'.format(used))
    }


def get_resources_info_from_pid(pid=None, *args, **kwargs):

    try:

        pid, memory_used_mb, cpu_percent = _get_info_from_pid(pid=pid)

        result = {
            'pid': pid,
            'memory_used_mb': memory_used_mb,
            'cpu_percent': cpu_percent,
        }

        result.update(kwargs)

        return result

    except psutil.NoSuchProcess:
        print('TODO: an error here')
