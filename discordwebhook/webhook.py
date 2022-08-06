"""
Creation of Webhooks
"""
from discordwebhook import allowedmentions, embed, errors, http, message, file, cache
from typing import List, Optional

Cache = cache.WebhookCache()

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
        url : Optional[str],
        #caching : bool = True
    ):
        
        self.url = url
        self.http = http.http()
        #self.caching = caching

        self.username = None 
        self.name = None 

        self.avatar_url = None 
        self.icon_url = None

        self.guild_id = None 
        self.channel_id = None 

        self.id = None 

        self.messages : List[message.WebhookMessage] = []

        #if caching:
        #    self._do_cache()
    
    def _do_cache(self):

        cachedWebhook = Cache.get_webhook(self.url)

        if cachedWebhook:

            self.username = cachedWebhook.username 
            self.name = self.username 

            self.avatar_url = cachedWebhook.avatar_url
            self.icon_url = self.avatar_url 

            self.guild_id = cachedWebhook.guild_id 
            self.channel_id = cachedWebhook.channel_id 

            self.id = cachedWebhook.id 

            self.messages = cachedWebhook.messages

        Cache._add_replace_webhook(self)
        

    def _build_from_data(self, data : dict):
        self.username = data["name"]
        self.name = self.username 
        self.avatar_url = data["avatar"]
        self.icon_url = self.avatar_url 

        self.id = data["id"]
        self.channel_id = data["channel_id"]
        self.guild_id = data["guild_id"]
        self.token = data["token"]
    
    def get_message(self, message_id : int) -> message.WebhookMessage | None:

        for _message in self.messages:
            if int(_message.id) == int(message_id):
                return _message 
        
        return None
    
    def _add_replace_message(self, message : message.WebhookMessage) -> None:
        if self.caching:

            cache_msg = self.get_message(message.id)

            if cache_msg:
                self.messages[ self.messages.index(cache_msg) ] = message 
            else:
                self.messages.append(message)

    def fetch_message_sync(self, message_id : int):
        
        return self.http.event_loop.run_until_complete(
            self.fetch_message_async(message_id)
        )
    
    async def fetch_message_async(self, message_id : int):

        data = await self.http.get_async(url=self.url + f"/messages/{message_id}")

        msg = message.WebhookMessage(self, data)

        self._add_replace_message(msg)

        return msg

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
                content, username, avatar_url, is_tts, embed, embeds, allowed_mentions, file, files
            )
        )

    async def send_async(self, 
        content : Optional[str] = None,
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
        
        raw = self._parse_options(username, avatar_url, is_tts, content, embed, embeds, allowed_mentions)

        ErrorHandling.requestErrors(self, raw)

        data = await self.http.request(
            "POST", 
            raw, 
            url=self.url, 
            params={"wait":"true"}, 
            files=[file] if files == [] and file else files
        )

        msg = message.WebhookMessage(self, data)

        self._add_replace_message(msg)

        return msg
    
    send = send_async 
    fetch_data = fetch_data_async
    fetch_message = fetch_message_async


    
