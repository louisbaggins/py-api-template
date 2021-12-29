class BotConfig:
    def __init__(self, json_config: dict) -> None:
        self.access_key = json_config['access-key']
        self.authorization_key = json_config['authorization-key']
        self.bot_id = json_config['bot-id']
