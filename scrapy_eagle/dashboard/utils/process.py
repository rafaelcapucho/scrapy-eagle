#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import psutil

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