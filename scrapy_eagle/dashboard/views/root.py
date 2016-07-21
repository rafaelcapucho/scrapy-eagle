import json
import flask


root = flask.Blueprint('root', __name__)


@root.route('/')
def index():

    return flask.render_template('index.html')
