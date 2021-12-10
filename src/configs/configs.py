from configs import SeqConfig, TimeConfig
from helpers import singleton
from json import load


@singleton
class Configs:

    def __init__(self):
        with open('./src/configs/configs.json', 'r') as config_data:
            self.raw_configs = load(config_data)
        self.append_configs()

    def append_configs(self):
        self.seq_config = SeqConfig(self.raw_configs['seq'])
        self.time_config = TimeConfig(self.raw_configs['time-config'])
