from .seq_config import SeqConfig
from .bot_config import BotConfig
from json import load


class Config():

    def __init__(self):
        with open('./src/configs/configs.json', 'r') as config_data:
            self.raw_configs = load(config_data)
        self.append_configs()

    def append_configs(self):
        self.seq_config = SeqConfig(self.raw_configs['seq'])
        self.bot_config = BotConfig(self.raw_configs['bot-config'])
