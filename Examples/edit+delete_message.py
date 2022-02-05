
import discordwebhook 
import time

# Initialise the webhook object.
webhook = discordwebhook.Webhook(
    url="webhook_url"
)

# Send a message to the webhook
message = webhook.send_sync(
    content="The message content goes here"
)
#message = webhook.fetch_message(message_id)

time.sleep(1) # wait 1 second before editing

# Edit the message with new content, but keep the embed (as it is left empty)
message.edit_sync(
    content="New message content! It has been 1 second since the webhook was sent"
)

time.sleep(5) # wait 5 seconds before deleting

message.delete_sync()
