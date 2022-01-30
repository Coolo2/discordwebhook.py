import datetime 


class Embed():
    def __init__(
        self,
        title : str = None,
        description : str = None,
        timestamp : datetime.datetime = None,
        color = None
    ):
        self.title = title 
        self.description = description 
        self.timestamp = timestamp
        self.color = color

        self.fields = []

        self.footer = None 
        self.image = None 
        self.video = None 
        self.thumbnail = None 
        self.author = None
    
    def set_footer(self, text : str, icon_url : str = None, proxy_icon_url : str = None):
        """Set embed footer"""
        self.footer = {"text":text, "icon_url":icon_url, "proxy_icon_url":proxy_icon_url}
    
    def set_image(self, url : str, proxy_url : str = None, height : int = None, width : int = None):
        """Set embed image: url, proxy_url, height, width"""
        self.image = {"url":url, "proxy_url":proxy_url, "height":height, "width":width}
    
    def set_video(self, url : str, proxy_url : str = None, height : int = None, width : int = None):
        """Set embed video: url, height, width"""
        self.video = {"url":url, "proxy_url":proxy_url, "height":height, "width":width}
    
    def set_thumbnail(self, url : str, proxy_url : str = None, height : int = None, width : int = None):
        """Set embed thumbnail: url, proxy_url, height, width"""
        self.thumbnail = {"url":url, "proxy_url":proxy_url, "height":height, "width":width}
    
    def add_field(self, name : str, value : str, inline : bool = True):
        """Create an embed field, stackable: name, value, inline (boolean)"""
        self.fields.append({"name":name, "value":value, "inline":inline})
    
    def set_author(self, name : str, url : str = None, icon_url : str = None, proxy_icon_url : str = None):
        """Set embed author: name, url, icon_url, proxy_icon_url"""
        self.author = {"name":name, "url":url, "icon_url":icon_url, "proxy_icon_url":proxy_icon_url}
    
    def to_dict(self):
        self.raw = {}

        if self.title:
            self.raw["title"] = self.title 
        if self.description:
            self.raw["description"] = self.description
        if self.timestamp:
            self.raw["timestamp"] = self.timestamp.isoformat()
        if self.color:
            self.raw["color"] = int(str(self.color), 0)
        if self.footer:
            self.raw["footer"] = self.footer
        if self.image:
            self.raw["image"] = self.image
        if self.thumbnail:
            self.raw["thumbnail"] = self.thumbnail
        if self.video:
            self.raw["video"] = self.video 
        if self.author:
            self.raw["author"] = self.author 
        
        if self.fields:
            self.raw["fields"] = self.fields 
        
        return self.raw
        
        