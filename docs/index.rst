
discordwebhook.py
==================

`PyPi page <https://pypi.org/project/discordwebhook.py/>`_ | `GitHub page <https://github.com/Coolo22/discordwebhook.py/>`_

`discordwebhook.py` is a Python Library for easily using discord webhooks in python

It is a lightweight, sync and async ready wrapper for Discord API Webhooks.

**Main features:**

* Modern
* Asynchronous and synchronous support
* In-built embed support - no need for another package such as discord.py 
* Methods for fetching discord webhook information and posting
* Easy to use, fully documented


Setup
-------------------

Installation:
~~~~~~~~~~~~~~

    ``pip install discordwebhook.py``

Or download it from the `PyPi page <https://pypi.org/project/discordwebhook.py/>`_

Import
~~~~~~~~

    ``import discordwebhook``

API Reference
--------------

discordwebhook.Webhook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: discordwebhook.Webhook
   :widths: 50 50
   :header-rows: 1

   * - Parameters
     - Methods
   * - url : Optional[str]
     - .send_sync
   * - 
     - .send_async

Parameters 
***********

    **url : Optional[str] = None** - An optional URL to overwrite the Webhook object

Webhook object 

All synchronous and async webhook usage functions are in this class

.fetch_data_sync(url = None)
#############################

Parameters 
***********

    **url : Optional[str] = None** - An optional URL to overwrite the Webhook object

*await*   .fetch_data_async(url = None)
###########################################

Parameters 
***********

    **url : Optional[str] = None** - An optional URL to overwrite the Webhook object

.send_sync(content = None, url = None, username = None, avatar_url = None, is_tts = False, embed = None, embeds = None, allowed_mentions = allowedmentions.AllowedMentions())
##############################################################################################################################################################################################

Parameters
***********

    **content : Optional[str] = None** - The content to add to the message

    **url : Optional[str] = None** - The url to send the message to. Overwrites Webhook.url if url already exists

    **username : Optional[str] = None** - Username to overwrite the webhook name 

    **avatar_url : Optional[str] = None** - The avatar url to overwrite the icon 

    **is_tts : Optional[bool] = False** - Whether the message sends with TTS enabled

    **embed : Optional[discordwebhook.Embed]** - Singular embed to add to the message 

    **embeds : Optional[List[discordwebhook.Embed]]** - Optional list of embeds 

    **allowed_mentions : Optional[discordwebhook.AllowedMentions]** - The allowed mentions for the message

Synchronously send a message to the webhook. 

Throws error if no url is provided (through the class or method)

*await* .send_async(content = None, url = None, username = None, avatar_url = None, is_tts = False, embed = None, embeds = None, allowed_mentions = allowedmentions.AllowedMentions())
##############################################################################################################################################################################################

Parameters
***********

    **content : Optional[str] = None** - The content to add to the message

    **url : Optional[str] = None** - The url to send the message to. Overwrites Webhook.url if url already exists

    **username : Optional[str] = None** - Username to overwrite the webhook name 

    **avatar_url : Optional[str] = None** - The avatar url to overwrite the icon 

    **is_tts : Optional[bool] = False** - Whether the message sends with TTS enabled

    **embed : Optional[discordwebhook.Embed]** - Singular embed to add to the message 

    **embeds : Optional[List[discordwebhook.Embed]]** - Optional list of embeds 

    **allowed_mentions : Optional[discordwebhook.AllowedMentions]** - The allowed mentions for the message

Aynchronously send a message to the webhook. 

Throws error if no url is provided (through the class or method)

discordwebhook.Embed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: discordwebhook.Embed
   :widths: 50 50
   :header-rows: 1

   * - Parameters
     - Methods
   * - title : Optional[str]
     - .set_footer
   * - description : Optional[str]
     - .set_image
   * - timestamp : Optional[datetime.datetime]
     - .set_video
   * - color
     - .set_thumbnail 
   * - 
     - .set_author 
   * - 
     - .add_field

Parameters 
***********

    **title : Optional[str] = None** - Add a title to the embed 

    **description : Optional[str] = None** - Add a description to the embed 

    **timestamp : Optional[datetime.datetime] = None** - Add a timestamp to the embed footer 

    **color = None** - Set embed color

Embed object

Create embeds in the exact same way as discord.py with this class

.set_footer(text, icon_url = None, proxy_icon_url = None)
##########################################################

Set the embed footer 

Parameters 
***********

    **text : str** - Set footer text. Required argument 

    **icon_url : Optional[str] = None** - Set footer icon url. Not required

    **proxy_icon_url : Optional[str] = None** - Proxy icon url. Not required

.set_image(url, proxy_url = None, height = None, width = None)
###################################################################

Add an image to the embed

Parameters 
***********

    **url : str** - Set footer text. Required argument 

    **proxy_url : Optional[str] = None** - Proxy image url. Not required

    **height : Optional[int] = None** - Custom image height. Not required

    **width : Optional[int] = None** - Custom image width. Not required

.set_video(url, proxy_url = None, height = None, width = None)
###################################################################

Add a video to the embed

Parameters 
***********

    **url : str** - Set footer text. Required argument 

    **proxy_url : Optional[str] = None** - Proxy image url. Not required

    **height : Optional[int] = None** - Custom image height. Not required

    **width : Optional[int] = None** - Custom image width. Not required

.set_thumbnail(url, proxy_url = None, height = None, width = None)
###################################################################

Set embed thumbnail

Parameters 
***********

    **url : str** - Set footer text. Required argument 

    **proxy_url : Optional[str] = None** - Proxy image url. Not required

    **height : Optional[int] = None** - Custom image height. Not required

    **width : Optional[int] = None** - Custom image width. Not required

.set_author(name, url = None, icon_url = None, proxy_icon_url = None)
############################################################################

Set the embed footer 

Parameters 
***********

    **name : str** - Set footer text. Required argument 

    **url : Optional[str] = None** - User URL. Not required

    **icon_url : Optional[str] = None** - Set footer icon url. Not required

    **proxy_icon_url : Optional[str] = None** - Proxy icon url. Not required

.add_field(name, value, inline = True)
##########################################################

Add a field to the embed. Same as discord.py

Parameters 
***********

    **name : str** - Field name. 

    **value : str** - Value of the embed field. Goes under the name

    **inline : Optional[bool] = True** - Whether the field is inline. Defaults True

Examples
---------------

Multiple different examples

Synchronous (Basic) Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import discordwebhook

    # Create the webhook. Parameter url="webhook_url" can be added here instead of in method .sendSync()
    webhook = discordwebhook.Webhook(
        url="webhook_url"
    )

    # OPTIONAL - Get webhook username and avatar (sends request to discord)
    webhook_data = webhook.fetch_data_sync()

    # Add embed with title "Embed title", same as discord.py
    embed = discordwebhook.Embed(
        title="Embed title",
    )

    # Add a field to the embed, exactly the same as discord.py
    embed.add_field(name="Field title", value="Exact same as discord.py, however can be used synchronously", inline=False)

    # Post webhook to URL synchronously
    webhook.send_sync(
        f"This webhook's original username was **{webhook_data.username}**", # Webhook message content
        username="Coolo2", # Overwrite webhook username, can also be defined when class is initialized
        embed=embed # Embeds can also be set with embeds=[embed]
    )

Asynchronous Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    
    import discordwebhook


    async def doWebhook():

        # Create the webhook. Parameter url="webhook_url" can be added here instead of in method .sendSync()
        webhook = discordwebhook.Webhook(
            url="webhook_url"
        )

        # OPTIONAL - Get webhook username and avatar (sends request to discord)
        webhook_data = await webhook.fetch_data_async()

        # Add embed with title "Embed title", same as discord.py
        embed = discordwebhook.Embed(
            title="Embed title",
        )

        # Add a field to the embed, exactly the same as discord.py
        embed.add_field(name="Field title", value="Exact same as discord.py, however can be used synchronously", inline=False)

        # Post webhook to URL synchronously
        await webhook.send_async(
            f"This webhook's original username was **{webhook_data.username}**", # Webhook message content
            username="Coolo2", # Overwrite webhook username, can also be defined when class is initialized
            embed=embed # Embeds can also be set with embeds=[embed]
        )

Fetch example 
~~~~~~~~~~~~~~~~~

.. code-block:: python 

    import discordwebhook 

    webhook = discordwebhook.Webhook(
        url="webhook_url"
    )

    # Can be used synchronously and asynchronously with fetch_data_async. Returns current Webhook class
    webhook.fetch_data_sync()

    print(webhook.id)
    print(webhook.url)

    print(webhook.name)
    print(webhook.icon_url)

    print(webhook.channel_id)
    print(webhook.guild_id)

More examples can be found at the `GitHub page Examples folder <https://github.com/Coolo22/discordwebhook.py/tree/master/Examples>`_ .


Version History
--------------------

1.0.1 - 30th January 2022 (current)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Rewritten the whole library. Too many changes to show, see documentation.

0.1.2 - 29th July 2020
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Added ability to set username and avatar_url in Webhook().send() with alias author

0.1.1 - 29th July 2020
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Fix version number issues with 0.1.0

0.1.0 - 29th July 2020
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Fixed asyncCreate not returning any values
* Added error handling for invalid token in fetching webhooks 
* Added error handling for no provided url
* Added ability for setting webhook link prior to sending it, adding a link to the create.Webhook object
* Added alias `discordwebhook.use` for `discordwebhook.create` and `discordwebhook.asyncUse` for `discordwebhook.asyncCreate`
* Many changes to documentation and other things

0.0.8 - 28th July 2020
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Fixed fatal error which occured with all embeds after 0.0.7

0.0.7 - 28th July 2020 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Added discordwebhook.discordwebhook
* `discordwebhook.fetch.Webhook()` now supports a Webhook() object instead of just string
* Changed `discordwebhook.discordwebhook.version.recent` to `current` with alias `recent`
* When using webhooks set information is stored in variables and can be accessed later by using (webhook).(setData), for example webhook.message
* Added message and tts kwarg to .send to allow for one line webhook sends
* Added kwargs to embed creation to create an experience identical to discord.py
* Added docstrings at the top of files
* Started error handling for embeds, checks on send to keep projects working

0.0.6 - 28th July 2020 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Fixed fatal errors with 0.0.5

0.0.5 - 28th July 2020
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Changed embed class so embed.embed can be replaced with just embed - simplifying sends
* Aditions and fixes to documentation
* Documentation addition to PyPi page 

0.0.4 - 28th July 2020 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Added mention permissions (if mentions will work)
* Reorganised some functions 
* Created documentation - Not listed on PyPi page 

0.0.3 - 28th July 2020
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Fixed fatal bugs with the previous release with asyncio 

0.0.2 - 28th July 2020
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Moved to a different name 
* Fixed bugs with original release 

0.0.1 - 28th July 2020
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Original release on another name 
* Added main features such as Webhook post and creation
* Added embeds
* Added asynchronous and synchronous functions
