import json
import flask


root = flask.Blueprint('root', __name__)


@root.route('/')
def index():

    return flask.render_template('index.html')

    # return flask.Response(
    #     response=json.dumps(results, sort_keys=True),
    #     status=200,
    #     mimetype="application/json"
    # )
