from discordwebhook import asyncCreate
#Importing asynchronous creation


async def SendWebhook(url):
    
    webhook = asyncCreate.Webhook(url)
    embed = asyncCreate.Embed(
        title="A simple embed title", 
        description="Simple embed description",
        color=0xFF0000)
    embed.add_field(name="simple field title", value="simple field value", inline=False)
    #Create a simple embed with one field, exactly the same as in discord.py

    await webhook.send(embed=embed)

#Creating an async function to send a webhook to a url. Uses the asynchronous section of the package
