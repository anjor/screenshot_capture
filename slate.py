import configparser
import requests


class Slate:

    def __init__(self, config_file="./slate.conf"):
        self.config_file = config_file
        self.api_key = self._parse_api_key()

    def _parse_api_key(self, section='DEFAULT'):
        config = configparser.ConfigParser()
        config.read(self.config_file)
        return config[section]['API_KEY']

    def _get_auth_header(self):
        return {"Authorization": self.api_key}

    def upload_files(self, files):
        url = "https://uploads.slate.host/api/v3/public"
        r = requests.post(url, headers=self._get_auth_header(), files=files)
        print(r.status_code)
