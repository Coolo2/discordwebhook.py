

class WebhookAttachment():
    def __init__(self, data : dict):
        self.id = int(data["id"])
        self.name = data["filename"]
        self.size = data["size"]
        self.url = data["url"]
        self.proxy_url = data["proxy_url"]