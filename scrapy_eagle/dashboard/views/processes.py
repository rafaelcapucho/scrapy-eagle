import json

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
