import json
from collections import OrderedDict
from datetime import datetime

import flask

from scrapy_eagle.dashboard import settings
from scrapy_eagle.dashboard.memory import get_job_object


jobs = flask.Blueprint('jobs', __name__)


@jobs.route('/update', methods=['GET', 'POST'])
def update():

    #TODO: Ensure that the incoming request comes from the same IP (Security)

    result = {}

    key = flask.request.form.get('key', None)
    active = flask.request.form.get('active', None)
    job_type = flask.request.form.get('job_type', None)
    frequency_minutes = flask.request.form.get('frequency_minutes', None)
    max_concurrency = flask.request.form.get('max_concurrency', None)
    min_concurrency = flask.request.form.get('min_concurrency', None)
    priority = flask.request.form.get('priority', None)
    start_urls = flask.request.form.get('start_urls', None)
    max_memory_mb = flask.request.form.get('max_memory_mb', None)

    print('max_concurrency: ', max_concurrency, type(max_concurrency))
    print('max_memory_mb: ', max_memory_mb, type(max_memory_mb))

    if not all([key, active, job_type, frequency_minutes, max_concurrency, min_concurrency, priority, max_memory_mb]):
        print('entro #1')
        result.update({
            'status': 'error',
            'msg': 'You are missing some information, please check your form.'
        })

    elif not start_urls and job_type == 'spider':
        result.update({
            'status': 'error',
            'msg': 'You should provide the Start URLs information for spiders.'
        })

    else:
        print('entro #3')
        result.update({
            'status': 'ok'
        })

    return flask.Response(
        response=json.dumps(result, sort_keys=True),
        status=200,
        mimetype="application/json"
    )


@jobs.route('/list', methods=['GET'])
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

        obj = get_job_object(key=s)

        if obj:
            d[s] = obj
        else:
            # TODO: How to proceed for newly jobs
            pass

        # d[s] = {}
        # d[s]['active'] = True
        # d[s]['job_type'] = 'spider' # or 'command'
        # d[s]['min_concurrency'] = 1
        # d[s]['max_concurrency'] = 5
        # d[s]['max_memory_mb'] = 200
        # d[s]['priority'] = 7
        # d[s]['frequency_minutes'] = 60
        # d[s]['last_started_at'] = 20
        # d[s]['start_urls'] = []
        # d[s]['last_started_at'] = datetime.utcnow().isoformat()

    # TODO: Iterate over all commands
    obj = get_job_object(key='generator')

    if obj:
        d['generator'] = obj

    # d['generator'] = {}
    # d['generator']['active'] = True
    # d['generator']['job_type'] = 'command'  # or 'command'
    # d['generator']['min_concurrency'] = 1
    # d['generator']['max_concurrency'] = 3
    # d['generator']['max_memory_mb'] = 50
    # d['generator']['priority'] = 2
    # d['generator']['frequency_minutes'] = 5
    # d['generator']['last_started_at'] = 20
    # d['generator']['start_urls'] = None

    return flask.Response(
        response=json.dumps(d, sort_keys=True),
        status=200,
        mimetype="application/json"
    )
