#recuperer les donnees depuis un lien


from model.CryptoModel import CryptoModel 
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class DataReader :
        def __init__(self):
                self._url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
                self._API_KEY = 'ded5b890-0e71-41e4-b097-a3e73ec43f99'
                self.parameters = {
                        'start': '1',
                        'limit': '20',
                        'convert': 'USD',
                        
                }
                self.headers = {
                        'Accepts': 'application/json',
                        'X-CMC_PRO_API_KEY': self._API_KEY
                }
                
        def get_data(self):
                session = Session()
                session.headers.update(self.headers)
                crypto_dict = {}

                try:
                        response = session.get(self._url, params=self.parameters)
                        data = json.loads(response.text)
                        for crypto_json in data['data']:
                                crypto = CryptoModel()
                                crypto.load(crypto_json)
                                crypto_dict[crypto.name] = crypto  # Ajouter la cryptomonnaie au dictionnaire en utilisant son nom comme clé
                except Exception as e:
                        return list(crypto_dict.values()) 

                return list(crypto_dict.values())  # Retourner la liste des cryptomonnaies