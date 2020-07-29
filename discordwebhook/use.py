"""
Creation of Webhooks and Embeds synchronously
"""
import requests, json, datetime
from discordwebhook import create

Embed = create.Embed
Webhook = create.Webhook
ErrorHandling = create.ErrorHandling