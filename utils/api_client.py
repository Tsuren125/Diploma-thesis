import os
from urllib.parse import urljoin
import requests
from dotenv import load_dotenv


load_dotenv()


API_BASE = os.getenv("API_BASE_URL", "https://reqres.in/api")




class ApiClient:
def __init__(self, base_url: str = API_BASE):
self.base_url = base_url.rstrip('/') + '/'
self.session = requests.Session()


def _url(self, path: str) -> str:
return urljoin(self.base_url, path.lstrip('/'))


def get(self, path: str, **kwargs):
return self.session.get(self._url(path), **kwargs)


def post(self, path: str, json=None, **kwargs):
return self.session.post(self._url(path), json=json, **kwargs)


def put(self, path: str, json=None, **kwargs):
return self.session.put(self._url(path), json=json, **kwargs)


def delete(self, path: str, **kwargs):
return self.session.delete(self._url(path), **kwargs)
