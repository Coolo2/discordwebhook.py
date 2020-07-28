from discordwebhook import fetch 
#Importing the file for fetching webhook information

webhook = fetch.Webhook("WEBHOOK_LINK")
#Creates a variable with all webhook information needed

print(f"""
The inputted webhook's name is: {webhook.name}
The inputted webhook's channel and guild id's are: {webhook.channel_id} and {webhook.guild_id}
The inputted webhook's ID and token are: {webhook.id} and {webhook.token}
""")
#Prints information about the webhook in the format provided
