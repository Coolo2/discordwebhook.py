from discordwebhook import asyncCreate
#Importing asynchronous creation


async def SendWebhook(url):
    
    webhook = asyncCreate.Webhook()
    embed = asyncCreate.Embed()

    embed.title("A simple embed title")
    embed.description("Simple embed description")
    embed.color(0xFF0000) # Red embed color 

    await webhook.send(url, embed=embed.embed)

#Creating an async function to send a webhook to a url. Uses the asynchronous section of the package
