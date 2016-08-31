from datetime import datetime

import json
import flask

from scrapy_eagle.dashboard.memory import get_connection


servers = flask.Blueprint('servers', __name__)


@servers.route('/list')
def listing():

    now = datetime.now()

    redis_conn = get_connection()

    _servers = redis_conn.zrangebyscore('eagle_servers', now.timestamp(), max='+inf')

    results = []

    for entry in _servers:
        parts = entry.decode('utf-8').split("-")
        ip, hostname = parts[0], "-".join(parts[1:])
        results.append({'public_ip': ip, 'hostname': hostname})

    # Sets in Redis usually returns in random order, sort by hostname
    results = sorted(results, key=lambda x: x['hostname'])

    return flask.Response(
        response=json.dumps(results, sort_keys=True),
        status=200,
        mimetype="application/json"
    )
