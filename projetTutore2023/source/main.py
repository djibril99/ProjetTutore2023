#code principale
import streamlit as st
import pandas as pd

from source.code.DataReader import DataReader


URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
API_KEY = 'ded5b890-0e71-41e4-b097-a3e73ec43f99'
data_reader = DataReader(URL, API_KEY)

data = data_reader.get_data()
if data is None:
        st.error('Error while loading data')
        st.stop()
else:
        print(data)
        df = pd.DataFrame(data)
        st.dataframe(df)
