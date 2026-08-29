import yaml
import os
from dotenv import load_dotenv

load_dotenv()
class ConfigReader:

    def __init__(self) :
        self.config = self._read_config()

    def _read_config(self):
        with open("config.yaml", 'r') as file:
            return yaml.safe_load(file)

    def get_environment(self):
        return self.config['environment']

    def get_browser(self):
        return self.config['browser']

    def get_timeout(self):
        return self.config['timeout']

    def get_headless(self):
        return self.config['headless']

    def get_base_url(self):
        env = self.get_environment()
        return self.config['environments'][env]['url']

    def get_invalid_user(self):
        return self.config['test_data']['invalid_user']["username"], self.config['test_data']['invalid_user']["password"]

    def get_locked_user(self):
        return self.config['test_data']['locked_user']["username"], self.config['test_data']['locked_user']["password"]

    def get_credential(self):
        return os.getenv("TEST_USERNAME"), os.getenv("TEST_PASSWORD")
