import flask


react_app = flask.Blueprint('app', __name__)


@react_app.route('/', defaults={'path': ''})
@react_app.route('/<path:path>')
def app(path):
    return flask.render_template('index.html')
