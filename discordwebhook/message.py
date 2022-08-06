from discordwebhook import author, http, embed, allowedmentions, attachment
from typing import Optional, List

class WebhookMessage():
    def __init__(self, webhook, data):

        self.http : http.http = webhook.http

        self.id = data["id"]
        self.content = data["content"]
        self.channel_id = data["channel_id"]
        self.attachments = [attachment.WebhookAttachment(a) for a in data["attachments"]]
        self.embeds = data["embeds"]
        self.mentions = data["mentions"]
        self.mention_roles = data["mention_roles"]
        self.pinned = data["pinned"]
        self.mention_everyone = data["mention_everyone"]
        self.is_tts = data["tts"]
        self.timestamp_string = data["timestamp"]
        self.edited_timestamp_string = data["edited_timestamp"]
        self.components = data["components"]

        self.author = author.WebhookAuthor(webhook, data["author"])

        self.webhook = webhook
    
    def _parse_options(
        self, 
        content : str = None,
        embed : embed.Embed = None,
        embeds : List[embed.Embed] = [],
        allowed_mentions : allowedmentions.AllowedMentions = allowedmentions.AllowedMentions()
    ):
        embedsBuild = []

        if embed:
            embedsBuild.append(embed.to_dict())

        if embeds:
            for embed in embeds:
                embedsBuild.append(embed.to_dict())
        
        data = {
            "content":content,
            "allowed_mentions":allowed_mentions.to_dict()
        }

        if embedsBuild != []:
            data["embeds"] = embedsBuild

        return data

    def edit_sync(
        self,
        content : Optional[str] = None,
        embed : Optional[embed.Embed] = None,
        embeds : Optional[List[embed.Embed]] = None,
        allowed_mentions : Optional[allowedmentions.AllowedMentions] = allowedmentions.AllowedMentions()
    ):

        return self.http.event_loop.run_until_complete(
            self.edit_async(content, embed, embeds, allowed_mentions)
        )
    
    def delete_sync(self):

        return self.http.event_loop.run_until_complete(self.delete_async())
    
    async def delete_async(self):

        return await self.http.request("DELETE", url=self.webhook.url + f"/messages/{self.id}")
        
    
    async def edit_async(
        self,
        content : Optional[str] = None,
        embed : Optional[embed.Embed] = None,
        embeds : Optional[List[embed.Embed]] = None,
        allowed_mentions : Optional[allowedmentions.AllowedMentions] = allowedmentions.AllowedMentions()
    ):

        raw = self._parse_options(
            content, embed, embeds, allowed_mentions
        )

        data = await self.http.request("PATCH", raw, url=self.webhook.url + f"/messages/{self.id}")

        return WebhookMessage(self.webhook, data)
