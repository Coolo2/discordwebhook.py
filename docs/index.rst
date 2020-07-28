###################
discordwebhook.py
###################

`PyPi page <https://pypi.org/project/discordwebhook.py/>`_ | `GitHub page <https://github.com/Coolo22/discordwebhook.py/>`_

| discordwebhook.py is a new PyPi project for easily using discord webhooks in python
| It is the first with synchronous and asynchronous options
| **Main features:**

    * Asynchronous and synchronous support
    * In-built embed support - no need for another package such as discord.py 
    * Methods for fetching discord webhook information from links aswell as posting to webhooks
    * Easy to use, fully documented

******************
Setup
******************

**Installation:**

    ``pip install discordwebhook.py``

Or download it from the `PyPi page <https://pypi.org/project/discordwebhook.py/>`_

**Importing:**

    Importing synchronous Webhook usage:
        ``from discordwebhook import create``

    Importing asynchronous Webhook usage (reccomended with discord.py):
        ``from discordwebhook import asyncCreate``
    
    Import Webhook fetching:
        ``from discordwebhook import fetch``
    
    Importing all together:
        ``from discordwebhook import fetch, create, asyncCreate``

#############################################
`discordwebhook`.create
#############################################

*************************
`.create`.Webhook()
*************************
    | Synchronous Webhook Creation
    | All synchronous webhook usage functions are in this class

**.message(message : str)**

Add a message to the webhook 

**.username(username :  string)**

Overrwrite webhook username / set username for the webhook

**.avatar_url(url : string)**

Overwrite webhook avatar url / set webhook avatar url

**.tts(boolean)**

Set if the webhook is a tts message 

**.allowed_mentions(user : boolean, everyone : boolean, roles : boolean)**

Set what mentions will work for the webhook - setting an option to False will disable mentions from working

**.send(webhook_url, embed=(.create.Embed() object), embeds=[array of .create.Embed() objects])**

Synchronously send a webhook to the webhook_url provided - Only works for discord webhook urls

| 

*************************
`.asyncCreate`.Webhook()
*************************
    | Asynchronous Webhook Creation
    | All asynchronous webhook creation/usage functions are in this class

**.message(message : str)**

Add a message to the webhook 

**.username(username :  string)**

Overrwrite webhook username / set username for the webhook

**.avatar_url(url : string)**

Overwrite webhook avatar url / set webhook avatar url

**.tts(boolean)**

Set if the webhook is a tts message 

**.allowed_mentions(user : boolean, everyone : boolean, roles : boolean)**

Set what mentions will work for the webhook - setting an option to False will disable mentions from working

**await .send(webhook_url, embed=(.create.Embed() object), embeds=[array of .create.Embed() objects])**

Asynchronously send a webhook to the webhook_url provided - Only works for discord webhook urls

| 

********************************************
`.create`.Embed() or `.asyncCreate`.Embed()
********************************************
    | Synchronous or asynchronous embed creation
    | All Embed creation functions are in these classes

**.title(title : string)**

Add a title to the embed

**.description(description : string)**

Add a description to the embed 

**.footer(text : string, icon_url : string, proxy_icon_url : string)**

Add a footer to the embed 

**.image(url : string, proxy_url : string, height : string, width : string)**

Add an image to the embed 

**.video(url : string, width : string, height : string)**

Add a video to the embed 

**.author(name : string, url : string, icon_url : string, proxy_icon_url : string)**

Add an author to the embed 

**.thumbnail(url : string, proxy_url : string, width : string, height : string)**

Set embed thumbnail

**.timestamp()**

Add a timestamp to the embed in current UTC time 

**.color(color : hex)**

Set embed color 

**.colour(color : hex)**

Alias for **.color**

**.add_field(name : string, value : string, inline : boolean : True)**

Add field to the embed

| 

#########################################
``discordwebhook``.fetch
#########################################

    | For fetching information - not creating, not sending
    | All synchronous as asynchronous is not needed 

********************************
``.fetch``.Webhook(url)
********************************

| Fetching webhook information from a given discord webhook url 
| Synchronous 

**.webhook** 

The raw webhook json 

**.id**

The webhook ID 

**.name**

The webhook name - default name shown on webhook usage 

**.avatar_url** 

The set avatar url of the webhook - a discord avatar url 

**.channel_id**

The channel id of the webhook 

**.guild_id**

The guild id of the webhook 

**.application_id**

The webhook application id

**.token**

The webhook token

**.url** 

The webhook URL (the inputted url)
