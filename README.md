# discordwebhook.py

![Downloads](https://img.shields.io/pypi/dm/discordwebhook.py)
![Version](https://img.shields.io/pypi/v/discordwebhook.py)
![Discord](https://img.shields.io/discord/937336250191458334?label=discord)


A python package for using discord webhooks. The only with asynchronous and synchronous options and fetching webhook information. A lightweight alternative to a full Discord API wrapper, just for webhooks.

For documentation see the [readthedocs page](https://discordwebhook.readthedocs.io/en/latest/)
For downloads see the [PyPi page](https://pypi.org/project/discordwebhook.py/)

For extra support join [the Discord server](https://discord.gg/5EhsXvShBE)



# Installation
```pip install discordwebhook.py```


## Examples

### Basic synchronous example
```python
import discordwebhook

# Create the webhook. Parameter url="webhook_url" can be added here instead of in method .sendSync()
webhook = discordwebhook.Webhook(
    url="webhook_url"
)

# OPTIONAL - Get webhook username and avatar (sends request to discord)
webhook_data = webhook.fetch_data_sync()

# Add embed with title "Embed title", same as discord.py
embed = discordwebhook.Embed(
    title="Embed title",
)

# Add a field to the embed, exactly the same as discord.py
embed.add_field(name="Field title", value="Exact same as discord.py, however can be used synchronously", inline=False)

# Post webhook to URL synchronously. Use await webhook.send_async to send asynchronously
webhook.send_sync(
    f"This webhook's original username was **{webhook_data.username}**", # Webhook message content
    username="Coolo2", # Overwrite webhook username, can also be defined when class is initialized
    embed=embed # Embeds can also be set with embeds=[embed]
)
```
### Fetch example
```python
import discordwebhook 

webhook = discordwebhook.Webhook(
    url="webhook_url"
)

# Can be used synchronously and asynchronously with fetch_data_async. Returns current Webhook class
webhook.fetch_data_sync()

print(webhook.id)
print(webhook.url)

print(webhook.name)
print(webhook.icon_url)

print(webhook.channel_id)
print(webhook.guild_id)
```
