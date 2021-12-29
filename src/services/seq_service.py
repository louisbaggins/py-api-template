from logging import Logger, getLogger, basicConfig
from ..configs import Config
import seqlog


class SeqService:

    def __init__(
        self,
        seq_config: Config
    ) -> None:
        self.configs = seq_config

    def setup(self) -> Logger:
        basicConfig()
        self.logger = getLogger('seq_logger')
        url = self.configs.seq_config.server_url
        api_key = self.configs.seq_config.api_key
        seq_handler = seqlog.log_to_seq(
            server_url=url, api_key=api_key, auto_flush=1000, batch_size=1)
        self.logger.addHandler(seq_handler)
        return self.logger
