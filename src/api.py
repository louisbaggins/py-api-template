from routes import PingRoute
from flask_restful import Resource, Api
from services import SeqService
from waitress import serve
from flask import Flask
from os import environ
from flask_swagger_ui import get_swaggerui_blueprint


SeqService().setup()

app = Flask(__name__)
api = Api(app)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

api.add_resource(PingRoute, '/ping')

if __name__ == '__main__':
    port = environ.get('PORT', 8090)
    serve(app, host='0.0.0.0', port=port)
