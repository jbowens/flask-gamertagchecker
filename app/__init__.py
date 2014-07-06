import os
from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='static')

app.config.from_pyfile('../config/default.cfg')

# Setup blueprints
from blueprints.main import main
app.register_blueprint(main)

# Serve some static files too
# @app.route('/css/<path:path>')
# def static_server(path):
#     full_path = os.path.join('static', 'css', path)
#     app.logger.debug('Looking for path %s', full_path)
#     app.logger.debug(os.path.isfile(full_path))
#     return app.send_static_file(full_path)
