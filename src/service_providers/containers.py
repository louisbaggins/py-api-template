from dependency_injector import providers, containers
from ..configs import Config
from ..services import SeqService


class Settings(containers.DeclarativeContainer):
    config = providers.Singleton(Config)


class Clients(containers.DeclarativeContainer):
    seq_service = providers.Singleton(SeqService, Settings.config)
