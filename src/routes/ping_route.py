from flask import request
from flask_restful import Resource


class PingRoute(Resource):

    def get(self):
        return 'Pong'
