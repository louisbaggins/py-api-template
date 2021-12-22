from flask_restful import Resource
from ..service_providers import Clients
from ..services import SeqService
from dependency_injector.providers import Singleton


class PingRoute(Resource):

    def __init__(
        self,
        seq_service: Singleton[SeqService] = Clients.seq_service
    ) -> None:
        self._logger = seq_service().logger

    def get(self):
        try:
            return 'Pong'
        except Exception as e:
            self._logger.error(e)
