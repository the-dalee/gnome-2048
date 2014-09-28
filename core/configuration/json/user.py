from model.configuration.user import UserConfig
import json
import sys


class UserConfigManager(object):
    def __init__(self, config_path):
        self.config_path = config_path

    def load(self):
        config = UserConfig()
        try:
            with open(self.config_path, 'r') as f:
                compiled = json.load(f)
                config.theme = compiled["theme"]
        except IOError:
            print("Error while reading config file", file=sys.stderr)
            config.load_defaults()
        return config

    def save(self, config):
        try:
            with open(self.config_path, 'w') as f:
                json.dump(config, f)
        except IOError:
            print("Error while writting config file")
