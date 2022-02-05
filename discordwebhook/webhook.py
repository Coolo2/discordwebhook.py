"""
Creation of Webhooks
"""
from discordwebhook import allowedmentions, embed, errors, http, message, file
from typing import List, Optional

class ErrorHandling:
    def requestErrors(self, webhook):
        for value in webhook["embeds"]:
            if "fields" in value:
                for field in value["fields"]:
                    if field["name"].replace(" ", "") == "" or field["value"] == "":
                        raise Exception("Cannot use an empty field value/name")

class Webhook():
    def __init__(
        self, 
        url : Optional[str] = None
    ):
        self.url = url
        self.http = http.http()

        self.username = None 
        self.name = None 

        self.avatar_url = None 
        self.icon_url = None

        self.guild_id = None 
        self.channel_id = None 

        self.id = None 
    
    def _build_from_data(self, data : dict):
        self.username = data["name"]
        self.name = self.username 
        self.avatar_url = data["avatar"]
        self.icon_url = self.avatar_url 

        self.id = data["id"]
        self.channel_id = data["channel_id"]
        self.guild_id = data["guild_id"]
        self.token = data["token"]
    
    def fetch_message_sync(self, message_id : int):
        return self.http.event_loop.run_until_complete(
            self.fetch_message_async(message_id)
        )
    
    async def fetch_message_async(self, message_id : int):
        if self.url == None:
            raise Exception("No url provided")  

        data = await self.http.get_async(url=self.url + f"/messages/{message_id}")

        return message.WebhookMessage(self, data)

    def modify_sync(
        self,
        name : str,
        channel_id : int
    ):
        return self.http.event_loop.run_until_complete(
            self.modify_async(name, channel_id)
        )
    
    async def modify_async(
        self,
        name : str,
        channel_id : int
    ):
        if self.url == None:
            raise Exception("No url provided")  
        
        data = await self.http.patch_async({"name":name, "channel_id":str(channel_id)}, url=self.url)

        self.id = data["id"]
        self.name = data["name"]
        self.channel_id = data["channel_id"]
        self.guild_id = data["guild_id"]
        self.token = data["token"]
        
        return self

    def delete_sync(self):
        return self.http.event_loop.run_until_complete(
            self.delete_async()
        )
    
    async def delete_async(self):
        if self.url == None:
            raise Exception("No url provided")  
        
        await self.http.request("DELETE", url=self.url)

    def fetch_data_sync(self):
        return self.http.event_loop.run_until_complete(
            self.fetch_data_async()
        )
    
    async def fetch_data_async(self):
        if self.url == None:
            raise Exception("No url provided")  
        
        data = await self.http.get_async(url=self.url)

        self._build_from_data(data)

        return self

    def to_dict(self):
        self.raw = {}

        embeds = []
        for embed in self.embeds:
            embeds.append(embed.to_dict())
        
        self.raw = {
            "content":self.content,
            "username":self.username,
            "avatar_url":self.avatar_url,
            "tts":self.is_tts,
            "embeds":embeds,
            "allowed_mentions":self.allowed_mentions.to_dict()
        }

        return self.raw
    
    
    
    def _parse_options(
        self, 
        username : str = None,
        avatar_url : str = None,
        is_tts : bool = False,
        content : str = None,
        embed : embed.Embed = None,
        embeds : List[embed.Embed] = [],
        allowed_mentions : allowedmentions.AllowedMentions = allowedmentions.AllowedMentions()
    ):
        if embeds == None:
            embeds = []
        if embed:
            embeds.append(embed)

        embedsBuild = []
        for embed in embeds:
            embedsBuild.append(embed.to_dict())

        return {
            "content":content,
            "username":username or self.username,
            "avatar_url":avatar_url or self.avatar_url,
            "tts":is_tts,
            "embeds":embedsBuild,
            "allowed_mentions":allowed_mentions.to_dict()
        }
    
    def send_sync(
        self, 
        content : Optional[str] = None,
        url : Optional[str] =None, 
        username : Optional[str] = None,
        avatar_url : Optional[str] = None,
        is_tts : Optional[bool] = False,
        embed : Optional[embed.Embed] = None,
        embeds : Optional[List[embed.Embed]] = None,
        allowed_mentions : Optional[allowedmentions.AllowedMentions] = allowedmentions.AllowedMentions(),
        file : file.File = None,
        files : List[file.File] = []
    ):

        return self.http.event_loop.run_until_complete(
            self.send_async(
                content, url, username, avatar_url, is_tts, embed, embeds, allowed_mentions, file, files
            )
        )

    async def send_async(self, 
        content : Optional[str] = None,
        url : Optional[str] = None, 
        username : Optional[str] = None,
        avatar_url : Optional[str] = None,
        is_tts : Optional[bool] = False,
        embed : Optional[embed.Embed] = None,
        embeds : Optional[List[embed.Embed]] = None,
        allowed_mentions : Optional[allowedmentions.AllowedMentions] = allowedmentions.AllowedMentions(),
        file : file.File = None,
        files : List[file.File] = []
    ):
        """send the webhook asynchronously"""

        if url != None:
            self.url = url
        elif self.url == None:
            raise Exception("No url provided")  
        
        raw = self._parse_options(username, avatar_url, is_tts, content, embed, embeds, allowed_mentions)

        ErrorHandling.requestErrors(self, raw)

        data = await self.http.request(
            "POST", 
            raw, 
            url=self.url, 
            params={"wait":"true"}, 
            files=[file] if files == [] and file else files
        )

        return message.WebhookMessage(self, data)


    
