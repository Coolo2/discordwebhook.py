import requests, json

class Webhook(object):
    def __init__(self, url):
        """Returns for Webhook information"""
        self.webhook = requests.get(url).json()
        self.id = int(self.webhook["id"])
        self.name = self.webhook["name"]
        self.avatar_url = self.webhook["avatar"]
        self.channel_id = self.webhook["channel_id"]
        self.guild_id = self.webhook["guild_id"]
        self.application_id = self.webhook["application_id"]
        self.token = self.webhook["token"]
        self.url = url
