from discordwebhook import create 
#Import webhook creation and usage

webhook = create.Webhook("WEBHOOK_URL")
#Create webhook object

webhook.message("Example TTS message", tts=True)
#or webhook.tts()

webhook.send() #Send webhook to given link
