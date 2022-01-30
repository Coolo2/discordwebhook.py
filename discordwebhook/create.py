purple = '\033[95m'
cyan = '\033[96m'
darkcyan = '\033[36m'
blue = '\033[94m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
bold = '\033[1m'
underline = '\033[4m'
end = '\033[0m'

class Webhook():
    def __init__(self, url=None, **kwargs):
        print(red + "This class has been depreciated! See the rewrite here https://github.com/Coolo22/discordwebhook.py" + end)
        print(f"""
You may have meant:

import discordwebhook

webhook = discordwebhook.Webhook(url="webhook_url")
webhook.send_sync(content="Message content here")

{red}See docs here: {end} https://github.com/Coolo22/discordwebhook.py
        """)

class Embed():
    def __init__(self):
        print(red + "This class has been depreciated! See the rewrite here https://github.com/Coolo22/discordwebhook.py" + end)
        print(f"""
You may have meant:

import discordwebhook

embed = discordwebhook.Embed(title="Title", description="Description")

{red}See docs here: {end} https://github.com/Coolo22/discordwebhook.py
        """)