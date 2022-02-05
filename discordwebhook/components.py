from typing import List
import discordwebhook

class ButtonStyle:
    primary = 1
    secondary = 2
    success = 3
    danger = 4
    link = 5

    blurple = primary
    grey = secondary
    green = success
    red = danger 
    url = link

# DO emoji API https://discord.com/developers/docs/resources/emoji

class Button():
    def __init__(self, style : ButtonStyle, label : str = None, emoji : str  = None, url : str = None):
        self.style = style 
        self.label = label 
        self.emoji = emoji 
        self.url = url
    
    def to_dict(self):
        return {
                    "type": 2,
                    "label": "Click me!",
                    "style": 1,
                    "custom_id": "click_one"
                }
class Row():
    def __init__(self, components : List[Button]):
        self.components = components
    
    def to_dict(self):
        return {
            "type":1,
            "components":[button.to_dict() for button in self.components]
        }