import asyncio
import json
import aiohttp 


class RateLmited(Exception):
  pass


class Client:

  def __init__(self):
    self.base = f"https://lichess.org/api"
    self.session = aiohttp.ClientSession()
    self.timeout = 10
    self.errors = {
      429 : RateLmited
    }
  
  async def _request(self, method, endpoint, data):
    url = self.base + endpoint
    async with self.session.request(method, url, json=data, timeout = self.timeout) as r:
      if r.status in list(self.errors.keys()):
        raise self.errors.get(r.status)
      
      return await r.json()

  async def post(self, endpoint, data):
    resp = await self._request("POST", endpoint, data)
    return(resp)

  async def get(self, endpoint):
    resp = await self._request("GET", endpoint, None)
    return(resp)

  async def put(self, endpoint, data):
    resp = await self._request("PUT", endpoint, data)
    return(resp)

  async def delete(self, endpoint):
    resp = await self._request("DELETE", endpoint, None)
    return(resp)


class LichessHTTP:
  def __init__(self):
    self.client = Client()
    
  async def create_open_challange(self, varient):
    endpoint = "/challenge/open"
    body = {"varient" : varient}
    resp = await self.client.post(endpoint, body)
    return resp




