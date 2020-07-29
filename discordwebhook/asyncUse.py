"""
Creation of Webhooks and Embeds synchronously
"""
import requests, json, datetime
from discordwebhook import asyncCreate

Embed = asyncCreate.Embed
Webhook = asyncCreate.Webhook
ErrorHandling = asyncCreate.ErrorHandling