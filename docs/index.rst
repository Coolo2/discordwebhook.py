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

#########################
`.asyncCreate`.Webhook()
#########################
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

##############
Examples
##############

General Example

.. code-block:: python

    from discordwebhook import create # Import discordwebhook create

    webhook = create.Webhook() # Create Webhook object
    embed = create.Embed() # Create embed object

    webhook.username("Example Webhook") # Override webhook username as 'Example Webhook'
    webhook.message("Hello! This is a message from an example webhook with the `discordwebhook.py` library!") # Message to go with the embed

    embed.title("Github Logo") # Embed title as 'Github Logo'
    embed.image(url="https://image.flaticon.com/icons/png/512/25/25231.png") # Embed image as github logo
    embed.color(0x808080) # Gray embed color

    webhook.send("WEBHOOK_URL", embed=embed) #Send webhook to given link with the embed

Fetch example 

.. code-block:: python 

    from discordwebhook import fetch 
    #Importing the file for fetching webhook information

    webhook = fetch.Webhook("WEBHOOK_LINK")
    #Creates a variable with all webhook information needed

    print(f"""
    The inputted webhook's name is: {webhook.name}
    The inputted webhook's channel and guild id's are: {webhook.channel_id} and {webhook.guild_id}
    The inputted webhook's ID and token are: {webhook.id} and {webhook.token}
    """)
    #Prints information about the webhook in the format provided

More examples can be found at the `GitHub page <https://github.com/Coolo22/discordwebhook.py/>`_ Examples folder.

|

##########################
Version History
##########################

*********************************
0.0.5 - 28th July 2020 (current)
*********************************

 | Changed embed class so embed.embed can be replaced with just embed - simplifying sends
 | Aditions and fixes to documentation

*********************************
0.0.4 - 28th July 2020 
*********************************

 | Added mention permissions (if mentions will work)
 | Reorganised some functions 
 | Created documentation - Not listed on PyPi page 

***********************
0.0.3 - 28th July 2020
***********************

 | Fixed fatal bugs with the previous release with asyncio 

***********************
0.0.2 - 28th July 2020
***********************

 | Moved to a different name 
 | Fixed bugs with original release 

***********************
0.0.1 - 28th July 2020
***********************

 | Original release on another name 
 | Added main features such as Webhook post and creation
 | Added embeds
 | Added asynchronous and synchronous functions
