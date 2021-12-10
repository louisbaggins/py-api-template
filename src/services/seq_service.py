from configs import Configs
from helpers import Singleton
import logging
import seqlog


class SeqService:

    def __init__(self):
        self.seq_config = Configs.instance().seq_config

    def setup(self):
        logging.basicConfig()
        self.logger = logging.getLogger('seq_logger')
        url = self.seq_config.server_url
        api_key = self.seq_config.api_key
        seq_handler = seqlog.log_to_seq(
            server_url=url, api_key=api_key, auto_flush=1000, batch_size=1)
        self.logger.addHandler(seq_handler)

        return self.logger
