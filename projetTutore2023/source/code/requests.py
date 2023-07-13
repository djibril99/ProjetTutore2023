#recuperer les donnees depuis un lien

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import streamlit as st
import pandas as pd


class DataReader :
        def __init__(self , lien:str, API_KEY):str
                self._url = lien
                self._API_KEY = API_KEY
                self.parameters = {
                        'start': '1',
                        'limit': '5',
                        'convert': 'USD'
                }
                self.headers = {
                        'Accepts': 'application/json',
                        'X-CMC_PRO_API_KEY': 'ded5b890-0e71-41e4-b097-a3e73ec43f99',
                }
                
        def get_data(self):
                
                session = Session()
                session.headers.update(self.headers)
                data = None
                try:
                        response = session.get(self.url, params=self.parameters)
                        data = json.loads(response.text)
                except Exception as e:
                        raise e 
                
                return data

