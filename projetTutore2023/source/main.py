import streamlit as st
import pandas as pd
from model.DataReader import DataReader
from model.CryptoModel import CryptoModel
from model.barChart import BarChart

# Récupérer les données depuis le lien
data_reader = DataReader()
liste_data = data_reader.get_data()

if len(liste_data) == 0:
    st.error('Error while loading data')
    st.stop()
else:
    df = pd.DataFrame(CryptoModel.data_array_to_json(liste_data))
    st.dataframe(df)

    # Utiliser la classe BarChart pour afficher le graphique
    bar_chart = BarChart(liste_data)
    fig = bar_chart.plot_prices()
    st.pyplot(fig)  # Affiche le graphique à l'aide de st.pyplot()
