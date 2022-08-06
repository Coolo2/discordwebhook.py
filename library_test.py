import discordwebhook

webhook = discordwebhook.Webhook()


async def test(webhook : discordwebhook.Webhook):

    webhook.send()

webhook.http.event_loop.run_until_complete(test(webhook))

