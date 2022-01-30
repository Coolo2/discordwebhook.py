
import discordwebhook


async def doWebhook():

    # Create the webhook. Parameter url="webhook_url" can be added here instead of in method .sendSync()
    webhook = discordwebhook.Webhook(
        url="webhook_url"
    )

    # OPTIONAL - Get webhook username and avatar (sends request to discord)
    webhook_data = await webhook.fetch_data_async()

    # Add embed with title "Embed title", same as discord.py
    embed = discordwebhook.Embed(
        title="Embed title",
    )

    # Add a field to the embed, exactly the same as discord.py
    embed.add_field(name="Field title", value="Exact same as discord.py, however can be used synchronously", inline=False)

    # Post webhook to URL synchronously
    await webhook.send_async(
        f"This webhook's original username was **{webhook_data.username}**", # Webhook message content
        username="Coolo2", # Overwrite webhook username, can also be defined when class is initialized
        embed=embed # Embeds can also be set with embeds=[embed]
    )