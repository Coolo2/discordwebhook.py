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