import streamlit as st
import matplotlib.pyplot as plt
from model.barChart import BarChart

#empeche le warning
st.set_option('deprecation.showPyplotGlobalUse', False)

def afficher_crypto_info(selected_crypto_name, liste_data):
    # Chercher la crypto-monnaie sélectionnée dans la liste de données
    selected_crypto_data = [crypto for crypto in liste_data if crypto.name == selected_crypto_name]
    if not selected_crypto_data:
        st.error(f"Crypto-monnaie '{selected_crypto_name}' introuvable.")
        return

    # Utiliser la classe BarChart pour afficher le graphique de variation de la crypto sélectionnée
    bar_chart = BarChart(liste_data)
    selected_crypto_data = selected_crypto_data[0]

    # Afficher les informations de la crypto sélectionnée
    st.write('Nom :', selected_crypto_data.name)
    st.write('Prix :', selected_crypto_data.price)
    st.write('Rang CMC :', selected_crypto_data.cmc_rank)
    # Ajouter si vous volulez...

    # Afficher le graphique de variation en 1 heure et 24 heures
    variation_1h_fig = bar_chart.plot_variation_1h(selected_crypto_data)
    variation_24h_fig = bar_chart.plot_variation_24h(selected_crypto_data)

    # Afficher les graphiques dans Streamlit(sans cette partie les graphiques sont générés mais pas affichés)
    st.pyplot(variation_1h_fig)
    st.pyplot(variation_24h_fig)

    # Lors du changement ceci permet d'effacer ....
    plt.close(variation_1h_fig)
    plt.close(variation_24h_fig)