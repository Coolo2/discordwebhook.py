

class WebhookAuthor():
    def __init__(self, webhook, data):

        self.bot = data["bot"]
        self.id = data["id"]
        self.name = data["username"]
        self.avatar_url = data["avatar"]
        self.discriminator = data["discriminator"]