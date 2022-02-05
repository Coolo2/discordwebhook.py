import discordwebhook 

# Initialise the webhook object.
webhook = discordwebhook.Webhook(
    url="webhook_url"
)

# webhook.delete_async() can be used to delete asynchronously
webhook.delete_sync()
