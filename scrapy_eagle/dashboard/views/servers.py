from datetime import datetime

import json
import flask

from scrapy_eagle.dashboard.memory import get_connection


servers = flask.Blueprint('servers', __name__)

# @servers.route('/', defaults={'page': 'index'})
# @servers.route('/<page>')
@servers.route('/')
def show():

    now = datetime.now()

    redis_conn = get_connection()

    servers = redis_conn.zrangebyscore('servers', now.timestamp(), max='+inf')

    results = []

    for entry in servers:
        ip, hostname = entry.decode('utf-8').split("-")
        results.append({'public_ip': ip, 'hostname': hostname})

    # Set in Redis usually returns in random order, sort by hostname
    results = sorted(results, key=lambda x: x['hostname'])

    return flask.Response(
        response=json.dumps(results, sort_keys=True),
        status=200,
        mimetype="application/json"
    )