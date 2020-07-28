from discordwebhook import create 
#Import webhook creation and usage

webhook = create.Webhook()
#Create webhook object

webhook.message("Example TTS message", tts=True)
#or webhook.tts()

webhook.send("WEBHOOK_URL") #Send webhook to given link
