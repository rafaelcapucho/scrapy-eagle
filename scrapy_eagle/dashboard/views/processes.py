import json

import flask
import gevent


processes = flask.Blueprint('processes', __name__)


@processes.route('/exec_command')
def exec_command():

    return "ok"

    # gevent.spawn(subsub, base_dir=BASE_DIR, spider="")
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
