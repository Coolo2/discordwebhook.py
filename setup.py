from distutils.core import setup
long_description="""
[![Downloads](https://pepy.tech/badge/discordwebhook-py)](https://pepy.tech/project/discordwebhook-py)
[![Downloads](https://pepy.tech/badge/discordwebhook-py/month)](https://pepy.tech/project/discordwebhook-py)
![Version](https://img.shields.io/pypi/v/discordwebhook.py)
![Discord](https://img.shields.io/discord/937336250191458334?label=discord)

A simple python package for posting to discord webhooks in python

Has asynchronous and synchronous options

[Discord](https://discord.gg/5EhsXvShBE)

Basic Synchronous Example

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
"""
version = "1.0.0"

setup(
  name = 'discordwebhook.py',         
  packages = ['discordwebhook'],   
  project_urls={
        "Documentation": "https://discordwebhook.readthedocs.io/en/latest",
        "Issue tracker": "https://github.com/Coolo22/discordwebhook.py/issues",
    },
  version = version,     
  license='MIT',       
  description = 'Easily using discord webhooks in python - asynchronous and synchronous - documented at https://discordwebhook.readthedocs.io/en/latest/', 
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Coolo2',                   
  author_email = 'itsxcoolo2@gmail.com',      
  url = 'https://github.com/Coolo22/discordwebhook.py',   
  download_url = 'https://github.com/Coolo22/discordwebhook.py/raw/master/Archive/discordwebhook.py-' + version + '.tar.gz',    
  keywords = ['discord', 'webhook', 'python', 'simple', 'post', 'asynchronous', 'synchronous'],   
  install_requires=['aiohttp', 'requests'],
  classifiers=[
    'Development Status :: 5 - Production/Stable', 
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)