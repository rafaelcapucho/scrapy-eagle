import json
import flask

from scrapy_eagle.dashboard import settings


spiders = flask.Blueprint('spiders', __name__)


@spiders.route('/list')
def listing():

    _spiders = settings.get_spiders()

    _spiders.sort()

    return flask.Response(
        response=json.dumps(_spiders, sort_keys=True),
        status=200,
        mimetype="application/json"
    )
