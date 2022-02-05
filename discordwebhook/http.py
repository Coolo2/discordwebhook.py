
import aiohttp
import json
import asyncio

import nest_asyncio

from discordwebhook import errors, file

from typing import List

_infinity = 99999999999

class http():
    def __init__(self):
        self.base = "https://discord.com/api/"
        self.headers = {
            "Content-Type": "application/json"
        }

        self.event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.event_loop)
        nest_asyncio.apply()
    
    def _check_errors(self, response : dict):
        if "allowed_mentions" in response:
            raise errors.MutuallyExclusiveError("Allowed mentions are mutually exclusive")

    def get_sync(self, path=None, url=None):
        return self.event_loop.run_until_complete(
            self.get_async(path=path, url=url)
        )
    
    def delete_sync(self, path=None, url=None):
        return self.event_loop.run_until_complete(
            self.delete_async(path=path, url=url)
        )
    
    def post_sync(self, data, path=None, url=None, params : dict = {}):

        return self.event_loop.run_until_complete(
            self.post_async(data=data, path=path, url=url, params=params)
        )
    
    def patch_sync(self, data, path=None, url=None, params : dict = {}):

        return self.event_loop.run_until_complete(
            self.patch_async(data=data, path=path, url=url, params=params)
        )

    # Async

    async def post_async(self, data, path=None, url=None, params : dict = {}):
        return await self.request("POST", data=data, path=path, url=url, params=params)

    async def get_async(self, path=None, url=None):
        return await self.request("GET", path=path, url=url)
    
    async def delete_async(self, path=None, url=None):
        return await self.request("DELETE", path=path, url=url)
    
    async def patch_async(self, data, path=None, url=None, params : dict = {}):
        return await self.request("PATCH", data=data, path=path, url=url, params=params)

    def request_sync(
        self, method : str, data = None, path = None, url = None, params : dict = {}, file : file.File = None
    ):
        return self.event_loop.run_until_complete(
            self.request(method, data, path, url, params, file)
        )

    async def request(
        self, method : str, data = None, path = None, url = None, params : dict = {}, files : List[file.File] = []
    ):
        if path != None:
            url = self.base + path
        
        headers = self.headers
        if data != None:
            data = json.dumps(data)
        
        if len(files) > 0:
            formdata = aiohttp.FormData()

            if len(files) == 1:
                file = files[0]
                formdata.add_field('file',file.open(), filename=file.name, content_type='application/octet-stream')
            else:
                for index, file in enumerate(files):
                    formdata.add_field(f'file{index}', file.open(), filename=file.name, content_type='application/octet-stream')

            headers = {}

            if data  != None:
                formdata.add_field("payload_json", data)
            
            data = formdata
        
        retry_after = _infinity

        while retry_after > 0:

            async with aiohttp.ClientSession() as session:
                
                async with session.request(method, url, data=data, headers=headers, params=params) as r:
                    
                    
                    # Rate limit handling
                    if r.status == 429:
                        retry_after = ((await r.json())["retry_after"] / 1000) + 0.5
                        await asyncio.sleep(retry_after + 1)
                    elif r.status == 413:
                        return errors.FileTooLarge("The file is too large. Must be below 8MB")
                    else:
                        retry_after = 0     

                        try:
                            r.raise_for_status()
                        except:
                            self._check_errors(await r.json())

                        try:
                            return await r.json()
                            
                        except aiohttp.ContentTypeError:
                            return None
        
        if file:
            file.close()