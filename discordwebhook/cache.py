from typing import List 

class WebhookCache():

    def __init__(self):
        self.webhooks : List = []
    
    def get_webhook(self, url : str):

        for webhook in self.webhooks:
            if webhook.url == url:
                return webhook 
        
        return None
    
    def _add_replace_webhook(self, webhook) -> None:

        cache_webhook = self.get_webhook(webhook.url)

        if cache_webhook:
            self.webhooks[ self.webhooks.index(cache_webhook) ] = cache_webhook 
        else:
            self.webhooks.append(webhook)
