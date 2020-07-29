"""
Creation of Webhooks and Embeds synchronously
"""
import requests, json, datetime

class ErrorHandling:
    def requestErrors(self, webhook):
        for value in webhook["embeds"]:
            if "fields" in value:
                for field in value["fields"]:
                    if field["name"].replace(" ", "") == "" or field["value"] == "":
                        raise Exception("Cannot use an empty field value/name")

class Webhook():
    def __init__(self, url=None):
        self.url = url
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
    
    def send(self, url=None, **kwargs):
        """send the webhook"""
        
        self.webhook["embeds"] = []
        
        if url == None:
            if self.url == None:
                raise Exception("No url provided")  
        else:
            self.url = url
            

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
            if "message" in kwargs:
                self.webhook["content"] = kwargs["message"]
                self.message = kwargs["message"]
            if "tts" in kwargs:
                if kwargs["tts"] == True or kwargs["tts"] == None:
                    self.webhook["tts"] = "true"
                    self.tts = True
                else:
                    self.tts = False

        ErrorHandling.requestErrors(self, self.webhook)

        result = requests.post(self.url, data=json.dumps(self.webhook), headers={"Content-Type": "application/json"})

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            return err
        else:
            return "Payload delivered successfully, code {}.".format(result.status_code)

class Embed():
    def __init__(self, **kwargs):
        self.embed = {}
        self.fields = []
        for item in ["title", "description", "color", "colour", "timestamp"]:
            if item in kwargs:
                if item == "colour":
                    self.embed["color"] = int(str(kwargs[item]), 0)
                elif item == "timestamp":
                    self.embed["timestamp"] = datetime.datetime.utcnow().isoformat()
                else:
                    self.embed[item] = kwargs[item]

    def description(self, description):
        """Set embed description"""
        self.embed["description"] = description
    
    def title(self, title):
        """Set embed title"""
        self.embed["title"] = title
    
    def footer(self, **kwargs):
        """Set embed footer"""
        self.embed["footer"] = kwargs
    
    add_footer, set_footer = footer, footer
    
    def image(self, **kwargs):
        """Set embed image: url, proxy_url, height, width"""
        self.embed["image"] = kwargs
    
    set_image = image
    
    def video(self, **kwargs):
        """Set embed video: url, height, width"""
        self.embed["video"] = kwargs
    
    set_video = video
    
    def thumbnail(self, **kwargs):
        """Set embed thumbnail: url, proxy_url, height, width"""
        self.embed["thumbnail"] = kwargs
    
    set_thumbnail = thumbnail
    
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
    
    set_author = author

    def color(self, color):
        """Set embed color"""
        self.embed["color"] = int(str(color), 0)
    
    colour = color

    
