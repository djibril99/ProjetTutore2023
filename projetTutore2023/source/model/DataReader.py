from .CryptoModel import CryptoModel 
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from requests_cache import CachedSession


# IF BUGS INSTALL THIS : pip install requests-cache
class DataReader:
    def __init__(self,limit):
        self._url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        self._API_KEY = 'ded5b890-0e71-41e4-b097-a3e73ec43f99'
        self.limit = limit
        self.parameters = {
            'start': '1',
            'limit': self.limit,
            'convert': 'USD',
        }
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': self._API_KEY
        }
        self.cache_expire_after = 60  # Cache expiration time in seconds

    #methode pour recuperer les donnees depuis l'api
    def get_data(self):
        
        with CachedSession(cache_name='crypto_cache', backend='sqlite', expire_after=self.cache_expire_after) as session:
            session.headers.update(self.headers)
            crypto_dict = {}
            
            try:
                response = session.get(self._url, params=self.parameters)
                # print(response.text)
                data = json.loads(response.text)
                for crypto_json in data['data']:
                    crypto = CryptoModel()
                    crypto.load(crypto_json)
                    if crypto.name not in crypto_dict.keys() :
                        crypto_dict[crypto.name] = crypto
            except Exception as e:
                print(e)
                return []
            
            return list(crypto_dict.values())
