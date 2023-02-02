import requests
import json
import configparser as cfg


class telegram_chatbot():

    def __init__(self, config):
        self.token = self.read_token_from_config_file(config)
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def get_updates(self, offset=None):
        url = self.base + "getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
            
        r = requests.get(url)
        print(url)
        print(json.loads(r.content))
        return json.loads(r.content)

    def send_message(self, msg, chat_id):
        url = self.base + "sendMessage?chat_id={}&text={}".format(chat_id, msg)
        if msg is not None:
            print(url)
            requests.get(url)

    def read_token_from_config_file(self, config):
        return '6001233339:AAHNS66TEM4v99pLwKKUVlv3WFYwaWAdBiE'
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds', 'token')

