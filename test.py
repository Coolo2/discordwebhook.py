
import discordwebhook 

webhook = discordwebhook.Webhook("https://canary.discord.com/api/webhooks/751856093264740443/O4C91-B0B2X7grjVgFLUrc0d_g_fdcKBh-U9FGygj-rYqF1urNnxw25b5jL96Xw5tlWb")

msg = webhook.fetch_message_sync(1005496216341200938)

msg.edit_sync(content="hellotest5", 
    embeds=[discordwebhook.Embed(title="hi", description="hello")]
)