import json
from collections import OrderedDict
from datetime import datetime

import flask

from scrapy_eagle.dashboard import settings


spiders = flask.Blueprint('spiders', __name__)


@spiders.route('/list')
def listing():

    _spiders = settings.get_spiders()

    # May happen to request this route before we've
    # the settings filled by the gevent async execution `green_threads.find_new_spiders`
    if not _spiders:
        return flask.Response(
            response=json.dumps({}, sort_keys=True),
            status=200,
            mimetype="application/json"
        )

    _spiders.sort()

    d = OrderedDict()

    for s in _spiders:
        d[s] = {}
        d[s]['min_concurrency'] = 1
        d[s]['max_concurrency'] = 5
        d[s]['max_memory_mb'] = 200
        d[s]['priority'] = 7
        d[s]['frequency_minutes'] = 60
        # d[s]['last_started_at'] = datetime.utcnow().isoformat()
        d[s]['last_started_at'] = 20

    return flask.Response(
        response=json.dumps(d, sort_keys=True),
        status=200,
        mimetype="application/json"
    )
