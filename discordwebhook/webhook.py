"""
Creation of Webhooks and Embeds synchronously
"""
from types import NoneType
from discordwebhook import allowedmentions, embed, errors
from typing import List, Optional

import requests 
import aiohttp 
import json

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

        self.username = None 
        self.name = None 

        self.avatar_url = None 
        self.icon_url = None

        self.guild_id = None 
        self.channel_id = None 

        self.id = None 

    def fetch_data_sync(self, url : Optional[str] = None):
        if url != None:
            self.url = url
        elif self.url == None:
            raise Exception("No url provided")  
        
        data = requests.get(self.url).json()

        self.username = data["name"]
        self.name = self.username 
        self.avatar_url = data["avatar"]
        self.icon_url = self.avatar_url 

        self.id = data["id"]
        self.channel_id = data["channel_id"]
        self.guild_id = data["guild_id"]
        self.token = data["token"]

        return self
    
    async def fetch_data_async(self, url : Optional[str] = None):
        if url != None:
            self.url = url
        elif self.url == None:
            raise Exception("No url provided")  
        
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url, headers={"Content-Type": "application/json"}) as response:
                data = await response.json()

                self.username = data["name"]
                self.name = self.username 
                self.avatar_url = data["avatar"]
                self.icon_url = self.avatar_url 

                self.id = data["id"]
                self.channel_id = data["channel_id"]
                self.guild_id = data["guild_id"]
                self.token = data["token"]

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
    
    def _check_errors(self, response : dict):
        if "allowed_mentions" in response:
            raise errors.MutuallyExclusiveError("Allowed mentions are mutually exclusive")
    
    def _parse_options(
        self, 
        username : str = None,
        avatar_url : str = None,
        is_tts : bool = False,
        content : str = None,
        embed : embed.Embed | NoneType = None,
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
        allowed_mentions : Optional[allowedmentions.AllowedMentions] = allowedmentions.AllowedMentions()
    ):
        """send the webhook synchronously"""

        if url != None:
            self.url = url
        elif self.url == None:
            raise Exception("No url provided")  
        
        raw = self._parse_options(username, avatar_url, is_tts, content, embed, embeds, allowed_mentions)

        ErrorHandling.requestErrors(self, raw)

        result = requests.post(self.url, data=json.dumps(raw), headers={"Content-Type": "application/json"})
        
        try:
            result.raise_for_status()
        except:
            self._check_errors(result.json())
    
    async def send_async(self, 
        content : Optional[str] = None,
        url : Optional[str] = None, 
        username : Optional[str] = None,
        avatar_url : Optional[str] = None,
        is_tts : Optional[bool] = False,
        embed : Optional[embed.Embed] = None,
        embeds : Optional[List[embed.Embed]] = None,
        allowed_mentions : Optional[allowedmentions.AllowedMentions] = allowedmentions.AllowedMentions()
    ):
        """send the webhook asynchronously"""

        if url != None:
            self.url = url
        elif self.url == None:
            raise Exception("No url provided")  
        
        raw = self._parse_options(username, avatar_url, is_tts, content, embed, embeds, allowed_mentions)

        ErrorHandling.requestErrors(self, raw)

        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, data=json.dumps(raw), headers={"Content-Type": "application/json"}) as response:
                try:
                    response.raise_for_status()
                except:
                    self._check_errors(await response.json())

    
