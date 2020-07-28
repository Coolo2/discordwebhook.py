import requests, json, datetime

class Webhook():
    def __init__(self):
        self.webhook = {}

    def Webhook(self):
        return self.webhook
    
    def author(self, username):
        """override the default username of the webhook"""
        self.webhook["username"] = username
        self.author = username
        return self.author
    
    username = author
    
    def avatar_url(self, url):
        """	override the default avatar of the webhook"""
        self.webhook["avatar_url"] = url
        self.avatar_url = url
        return self.avatar_url
    
    def tts(self, boolean=None):
        """set if this is a TTS message"""
        if boolean == True or boolean == None:
            self.webhook["tts"] = "true"
            self.tts = True
        else:
            self.tts = False
        return self.tts
    
    def message(self, text, **kwargs):
        """the message contents (up to 2000 characters)"""
        if "tts" in kwargs:
            if kwargs["tts"] in [True, "true", "True"]:
                self.webhook["tts"] = "true"
                self.tts = True
        if text:
            self.webhook["content"] = text
            self.message = text
            return self.message
            
    
    def allowed_mentions(self, **kwargs):
        """options for if mentions are allowed from the webhook: everyone, roles, users"""
        finallist = []
        for item in ["users", "everyone", "roles"]:
            if item not in kwargs or kwargs[item] != False:
                finallist.append(item)

        self.webhook["allowed_mentions"] = {"parse":finallist}
        self.allowed_mentions = finallist

        return self.allowed_mentions
    
    def send(self, WebhookURL, **kwargs):
        """send the webhook"""
        
        self.webhook["embeds"] = []
        self.url = WebhookURL

        if kwargs != {}:
            if "embed" in kwargs:
                if type(kwargs["embed"]) is list:
                    for item in kwargs["embed"]:
                        self.webhook["embeds"].append(item.embed)
                else:
                    self.webhook["embeds"].append(kwargs["embed"].embed)
            if "embeds" in kwargs:
                if type(kwargs["embeds"]) is list:
                    for item in kwargs["embeds"]:
                        self.webhook["embeds"].append(item.embed)
                else:
                    self.webhook["embeds"].append(kwargs["embeds"].embed)


        result = requests.post(WebhookURL, data=json.dumps(self.webhook), headers={"Content-Type": "application/json"})

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            return err
        else:
            return "Payload delivered successfully, code {}.".format(result.status_code)

class Embed():
    def __init__(self):
        self.embed = {}
        self.fields = []

    def description(self, description):
        """Set embed description"""
        self.embed["description"] = description
    
    def title(self, title):
        """Set embed title"""
        self.embed["title"] = title
    
    def footer(self, **kwargs):
        """Set embed footer"""
        self.embed["footer"] = kwargs
    
    def image(self, **kwargs):
        """Set embed image: url, proxy_url, height, width"""
        self.embed["image"] = kwargs
    
    def video(self, **kwargs):
        """Set embed video: url, height, width"""
        self.embed["video"] = kwargs
    
    def thumbnail(self, **kwargs):
        """Set embed thumbnail: url, proxy_url, height, width"""
        self.embed["thumbnail"] = kwargs
    
    def add_field(self, **kwargs):
        """Create an embed field, stackable: name, value, inline (boolean)"""
        if "inline" not in kwargs:
            kwargs["inline"] = "true"
        self.fields.append(kwargs)
        self.embed["fields"] = self.fields
    
    def timestamp(self):
        """Add timestamp to an embed: text, icon_url, proxy_icon_url"""
        self.embed["timestamp"] = datetime.datetime.utcnow().isoformat()
    
    def author(self, **kwargs):
        """Set embed author: name, url, icon_url, proxy_icon_url"""
        self.embed["author"] = kwargs

    def color(self, color):
        """Set embed color"""
        self.embed["color"] = int(str(color), 0)
    
    colour = color

    
