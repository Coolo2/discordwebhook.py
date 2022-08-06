from setuptools import setup, Extension

version = "1.1.1"

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
  long_description=open("README.md").read(),
  long_description_content_type='text/markdown',
  author = 'Coolo2',                   
  author_email = 'itsxcoolo2@gmail.com',      
  url = 'https://github.com/Coolo22/discordwebhook.py',   
  download_url = 'https://github.com/Coolo22/discordwebhook.py/raw/master/Archive/discordwebhook.py-' + version + '.tar.gz',    
  keywords = ['discord', 'webhook', 'python', 'api', 'post', 'asynchronous', 'synchronous'],   
  install_requires=['aiohttp', 'nest_asyncio'],
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