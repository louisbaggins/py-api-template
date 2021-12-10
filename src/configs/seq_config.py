class SeqConfig:

    def __init__(self, json_config):
        self.server_url = json_config['server-url']
        self.api_key = json_config['api-key']
