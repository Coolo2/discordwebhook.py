import discordwebhook 

# Initialise the webhook object.
webhook = discordwebhook.Webhook(
    url="webhook_url"
)

# webhook.modify_async() can be used to modify asynchronously
webhook.modify_sync(
    name="New webhook name",
    channel_id=0 # Integer channel id to move webhook to.
)
