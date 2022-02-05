
import discordwebhook

# Create the webhook.
webhook = discordwebhook.Webhook(
    url="webhook_url"
)

# Add embed with title "Embed title", same as discord.py
embed = discordwebhook.Embed(
    title="Embed title",
)

# Add a field to the embed, exactly the same as discord.py
embed.add_field(name="Field title", value="Exact same as discord.py, however is lighter", inline=False)

# Post webhook to URL synchronously. Can be await webhook.send_async to send asynchronously
webhook.send_sync(
    f"This is the message content!", # Webhook message content
    username="Coolo2", # Overwrite webhook username, can also be defined when class is initialized
    embed=embed # Embeds can also be set with embeds=[embed]
)