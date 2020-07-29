# discordwebhook.py 0.1.2
A python package for using discord webhooks. The only with asynchronous and synchronous options and fetching webhook information. Useful for projects which may require the use of discord.py or projects that dont

[Documentation](https://discordwebhook.readthedocs.io/en/latest/) | [PyPi](https://discordwebhook.readthedocs.io/en/latest/)

Installation
```
pip install discordwebhook.py
```

Basic example
```python
from discordwebhook import create # Import discordwebhook create

webhook = create.Webhook("WEBHOOK_URL") # Create Webhook object


webhook.username("Example Webhook") # Override webhook username as 'Example Webhook'
webhook.message("Hello! This is a message from an example webhook with the `discordwebhook.py` library!") # Message to go with the embed

embed = create.Embed(title="Github Logo", color=0x808080) # Create embed object, Embed title as 'Github Logo', Gray embed color
embed.set_image(url="https://image.flaticon.com/icons/png/512/25/25231.png") # Embed image as github logo

webhook.send(embed=embed) #Send webhook to given link with the embed
```
Example with a fully formatted embed, message, custom username 
