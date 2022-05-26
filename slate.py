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

    def _get_upload_header(self):
        header = self._get_auth_header()
        header["Content-Type"] = "image/png"
        return header

    def upload_files(self, files):
        url = "https://uploads.slate.host/api/v3/public"
        for file in files:
            upload_file = {"file": open(file, 'rb')}
            print("Uploading file " + file)
            r = requests.post(url, headers=self._get_auth_header(), files=upload_file)
            if r.status_code == 200:
                print("Uploaded file: " + file)
            else:
                print("Failed to upload file: " + file, r.status_code)

            print(r.json())
