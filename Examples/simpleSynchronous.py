from discordwebhook import create 

webhook = create.Webhook("webhook_url")
embed = create.Embed()
#Creating the webhook, input a url for it to be sent and embed objects to use

embed.title("Embed title")
embed.add_field(name="Just a value title", value="Exactly the same as discord.py", inline=False)
#Setting title and adding a field, very similar to discord.py

webhook.username("Webhook username overwritten")
webhook.message("A message to go with the embed!")
#Setting webhook username and message (these are optional)

webhook.send(embeds=[embed]) 
#embeds can be embed without a list 
