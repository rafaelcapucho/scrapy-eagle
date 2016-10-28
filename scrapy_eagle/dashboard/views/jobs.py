import json
from collections import OrderedDict
from datetime import datetime, timedelta

import flask

from scrapy_eagle.dashboard import settings
from scrapy_eagle.dashboard.memory import get_job_object, update_job_object


jobs = flask.Blueprint('jobs', __name__)


@jobs.route('/update', methods=['POST'])
def update():

    #TODO: Ensure that the incoming request comes from the same IP (Security)

    result = {}
    error = False

    key, job_type, active, frequency_minutes, max_concurrency = (None, None, None, None, None)
    min_concurrency, priority, max_memory_mb, start_urls = (None, None, None, None)

    try:

        key = flask.request.form.get('key', None)
        job_type = flask.request.form.get('job_type', None)
        frequency_minutes = int(flask.request.form.get('frequency_minutes', None))
        max_concurrency = int(flask.request.form.get('max_concurrency', None))
        min_concurrency = int(flask.request.form.get('min_concurrency', None))
        priority = int(flask.request.form.get('priority', None))
        max_memory_mb = int(flask.request.form.get('max_memory_mb', None))
        start_urls = flask.request.form.get('start_urls', None)

        if flask.request.form.get('active', None) == 'false':
            active = False
        elif flask.request.form.get('active', None) == 'true':
            active = True
        else:
            active = False

    # Never trust in the user input type
    except ValueError:
        error = True
        result.update({
            'status': 'error',
            'msg': 'You sent wrong datatypes, like a letter when it should be numeric.'
        })

    if not error:

        if not all([key, job_type, frequency_minutes, max_concurrency, min_concurrency, priority, max_memory_mb]):
            error = True
            result.update({
                'status': 'error',
                'msg': 'You are missing some information, please check your form.'
            })

        elif not start_urls and job_type == 'spider':
            error = True
            result.update({
                'status': 'error',
                'msg': 'You should provide the Start URLs information for spiders.'
            })

        else:

            actual_obj = get_job_object(key=key)

            # A brand new
            if not actual_obj:
                actual_obj = {}

            actual_obj.update({
                'active': active,
                'job_type': job_type,
                'frequency_minutes': frequency_minutes,
                'max_concurrency': max_concurrency,
                'min_concurrency': min_concurrency,
                'priority': priority,
                'max_memory_mb': max_memory_mb
            })

            if job_type == 'spider':
                actual_obj.update({'start_urls': [x for x in start_urls.split("\n") if x]})

            update_job_object(key=key, fields=actual_obj)

        if not error:
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
    _commands = settings.get_commands()

    # When the system is starting up, spiders may return empty because
    # we're using async execution `green_threads.find_new_spiders`.
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
            # Jobs without previous information, using default config
            d[s] = {}
            d[s]['active'] = True
            d[s]['job_type'] = 'spider'
            d[s]['min_concurrency'] = 1
            d[s]['max_concurrency'] = 5
            d[s]['max_memory_mb'] = 200
            d[s]['priority'] = 7
            d[s]['frequency_minutes'] = 60
            d[s]['start_urls'] = []
            d[s]['last_started_at'] = datetime.utcnow().isoformat()
            d[s]['next_execution_at'] = (datetime.utcnow() + timedelta(minutes=d[s]['frequency_minutes'])).isoformat()

    for file_name in _commands:

        obj = get_job_object(key=file_name)

        if obj:
            d[file_name] = obj

        else:
            d[file_name] = {}
            d[file_name]['active'] = False
            d[file_name]['job_type'] = 'command'
            d[file_name]['min_concurrency'] = 1
            d[file_name]['max_concurrency'] = 3
            d[file_name]['max_memory_mb'] = 50
            d[file_name]['priority'] = 2
            d[file_name]['frequency_minutes'] = 60
            d[file_name]['last_started_at'] = None
            d[file_name]['next_execution_at'] = None

    return flask.Response(
        response=json.dumps(d, sort_keys=True),
        status=200,
        mimetype="application/json"
    )
