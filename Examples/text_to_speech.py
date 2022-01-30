
import discordwebhook 

# Create webhook with is_tts enabled
webhook = discordwebhook.Webhook(
    url="webhook_url"
)

# Send webhook synchronously. Method .sendAsync can also be used
webhook.send_sync(
    content="This is a TTS message!",
    is_tts=True
)