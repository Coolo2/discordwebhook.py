# discordwebhook.py 0.0.6
A python package for using discord webhooks. The only with asynchronous and synchronous options and fetching webhook information. Useful for projects which may require the use of discord.py or projects that dont

Installation
```
pip install discordwebhook.py
```

Basic example
```python
from discordwebhook import create # Import discordwebhook create

webhook = create.Webhook() # Create Webhook object
embed = create.Embed() # Create embed object

webhook.username("Example Webhook") # Override webhook username as 'Example Webhook'
webhook.message("Hello! This is a message from an example webhook with the `discordwebhook.py` library!") # Message to go with the embed

embed.title("Github Logo") # Embed title as 'Github Logo'
embed.image(url="https://image.flaticon.com/icons/png/512/25/25231.png") # Embed image as github logo
embed.color(0x808080) # Gray embed color

webhook.send("WEBHOOK_URL", embed=embed) #Send webhook to given link with the embed
```
Example with a fully formatted embed, message, custom username 
