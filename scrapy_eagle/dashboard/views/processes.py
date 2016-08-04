import os
import json
import signal

import flask
import gevent

from scrapy_eagle.dashboard.utils import processkit
from scrapy_eagle.dashboard import settings


processes = flask.Blueprint('processes', __name__)


@processes.route('/exec_command')
def exec_command():

    gevent.spawn(
        processkit.new_subprocess,
        base_dir='.',
        subprocess_pids=settings.subprocess_pids,
        queue_info_global=settings.queue_info_global,
        buffers=settings.buffers
    )

    result = {
        'status': True
    }

    return flask.Response(
        response=json.dumps(result, sort_keys=True),
        status=200,
        mimetype="application/json"
    )


@processes.route('/read_buffer/<int:pid>')
def read_buffer(pid):

    if not settings.buffers.get(pid):
        return flask.Response(
            response=json.dumps(
                {'status': False, 'msg': 'PID Not Found'},
                sort_keys=True
            ),
            status=200,
            mimetype="application/json"
        )

    def generate():

        sent = 0

        while not settings.buffers[pid]['finished']:

            for i, row in enumerate(settings.buffers[pid]['lines'][sent:]):

                sent += 1

                yield row+'<br>'

            gevent.sleep(0.5)

    return flask.Response(
        response=generate(),
        status=200,
        mimetype="text/html"
    )


@processes.route('/kill_subprocess/<int:pid>')
def kill_subprocess(pid):

    safe = False

    for _pid, _, _, _, _ in settings.subprocess_pids:

        if pid == _pid:
            safe = True
            break

    if safe:
        os.kill(pid, signal.SIGHUP)

        result = {
            'status': True,
            'msg': 'SIGHUP signal sent to PID {0}'.format(pid)
        }

    else:
        result = {
            'status': False,
            'msg': 'PID Not Found'
        }

    return flask.Response(
        response=json.dumps(result, sort_keys=True),
        status=200,
        mimetype="application/json"
    )

@processes.route('/start_spider/<spider>')
def start_spider(spider):

    _config = settings.get_config_file()

    command = [_config.get('scrapy', 'binary'), 'crawl', spider]

    # TODO: Verify if base_dir is set before use it

    gevent.spawn(
        processkit.new_subprocess,
        base_dir=_config.get('scrapy', 'base_dir'),
        command=command,
        spider=spider,
        subprocess_pids=settings.subprocess_pids,
        queue_info_global=settings.queue_info_global,
        buffers=settings.buffers
    )

    result = {
        'status': True
    }

    return flask.Response(
        response=json.dumps(result, sort_keys=True),
        status=200,
        mimetype="application/json"
    )