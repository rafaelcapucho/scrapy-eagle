import json

import flask
import gevent

from scrapy_eagle.dashboard.utils import processkit
from scrapy_eagle.dashboard.settings import get_config


processes = flask.Blueprint('processes', __name__)


@processes.route('/exec_command')
def exec_command():

    config = get_config()

    """gevent.spawn(
        processkit.new_subprocess,
        base_dir='.',
        subprocess_pids=config.subprocess_pids,
        queue_info_global=config.queue_info_global,
        buffers=config.buffers
    )"""

    return "ok"

    #
    # result = {
    #     'status': True
    # }
    #
    # return flask.Response(
    #     response=json.dumps(result, sort_keys=True),
    #     status=200,
    #     mimetype="application/json"
    # )
