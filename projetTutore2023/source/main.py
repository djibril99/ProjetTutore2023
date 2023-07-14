#code principale
import streamlit as st
import pandas as pd

from model.DataReader import DataReader
from model.CryptoModel import CryptoModel
#recuperer les donnees depuis du lien

data_reader = DataReader()
#recuperer la liste des donnees (liste de CryptoModel) depuis le lien de l'API
liste_data = data_reader.get_data()
                                      
if len(liste_data) == 0:
        st.error('Error while loading data')
        st.stop()
else:
        df = pd.DataFrame(CryptoModel.data_array_to_json(liste_data))
        
        x=st.dataframe(df)
        print(x)
