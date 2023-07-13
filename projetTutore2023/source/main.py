#code principale
import streamlit as st
import pandas as pd
from json import dumps

from source.code.DataReader import DataReader
from source.code.CryptoModel import CryptoModel

###########################################
#recuperer les donnees depuis du lien

URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
API_KEY = 'ded5b890-0e71-41e4-b097-a3e73ec43f99'
data_reader = DataReader(URL, API_KEY)

liste_data = data_reader.get_data()
if len(liste_data) == 0:
        st.error('Error while loading data')
        st.stop()
else:
        #convertir la liste en dictionnaire
        data_json = {}
        #recuperer les attritus de la classe CryptoModel
        
        listeKeys = [key for key in CryptoModel().__dict__]
        for key in listeKeys:
                data_json[key] = []
        for crypto_data in liste_data:
                #ajouter les donnees de chaque objet dans la liste
                dict_crupto = crypto_data.__dict__
                for key in listeKeys:
                        data_json[key].append(dict_crupto[key])
                        
                
                
        df = pd.DataFrame(data_json)
        st.dataframe(df)
