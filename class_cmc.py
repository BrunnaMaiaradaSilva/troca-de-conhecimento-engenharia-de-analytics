#Contruindo uma classe para fazermos chamadas a API
import secrets
import requests
from requests import Session

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': secrets.API_KEY,
}

class CMC:

    def __init__(self, token):
        
        self.apiurl = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
        self.headers = headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': secrets.API_KEY,}
        self.session = Session()
        self.session.headers.update(headers=headers)