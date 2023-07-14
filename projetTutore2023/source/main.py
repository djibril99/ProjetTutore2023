import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from model.DataReader import DataReader
from model.CryptoModel import CryptoModel

# Récupérer les données depuis le lien
data_reader = DataReader()
liste_data = data_reader.get_data()

if len(liste_data) == 0:
    st.error('Error while loading data')
    st.stop()
else:
    df = pd.DataFrame(CryptoModel.data_array_to_json(liste_data))

    # Afficher les informations de chaque crypto sur une seule ligne avec un en-tête
    for index, row in df.iterrows():
        expander = st.expander(f'{row["name"]} ({row["symbol"]})')
        with expander:
            st.write(f'Price: {row["price"]}')
            st.write(f'CMC Rank: {row["cmc_rank"]}')
            st.write(f'Num Market Pairs: {row["num_market_pairs"]}')
            st.write(f'Volume 24h: {row["volume_24h"]}')
            st.write(f'Percent Change 1h: {row["percent_change_1h"]}')
            
            # Créer un graphe spécifique à la crypto-monnaie
            fig, ax = plt.subplots()
            ax.plot(["1h", "24h", "7 jours"], [row["percent_change_1h"], row["percent_change_24h"], row["percent_change_7d"]])
            ax.set_xlabel('Variation')
            ax.set_ylabel('Temps')
            ax.set_title('Variations de la crypto-monnaie')
            for i, value in enumerate([row["percent_change_1h"], row["percent_change_24h"], row["percent_change_7d"]]):
                rounded_value = round(value, 2)  # Arrondir à deux chiffres après la virgule
                plt.text(i, value, f"{rounded_value}", color='red', ha='left', va='top')
            st.pyplot(fig)
