import streamlit as st
import matplotlib.pyplot as plt
from view.barChart import BarChart

def afficher_crypto_info(selected_crypto_name, liste_data):
    if not selected_crypto_name:
        st.warning("Veuillez sélectionner une crypto-monnaie")
        return

    # Chercher la crypto-monnaie sélectionnée dans la liste de données
    selected_crypto_data = [crypto for crypto in liste_data if crypto.name in selected_crypto_name]

    if not selected_crypto_data:
        st.warning("Aucune crypto-monnaie correspondante trouvée")
        return

    # Utiliser la classe BarChart pour afficher le graphique de variation de la crypto sélectionnée
    bar_chart = BarChart(liste_data)
    for crypto_data in selected_crypto_data:
        # Afficher les informations de la crypto sélectionnée
        st.write('Nom :', crypto_data.name)
        st.write('Prix :', crypto_data.price)
        st.write('Rang CMC :', crypto_data.cmc_rank)
        st.write('Nombre de paires de marché :', crypto_data.num_market_pairs)
        st.write('Volume 24h :', crypto_data.volume_24h)

        # Ajouter si vous le souhaitez...
        Variation_fig = bar_chart.plot_crypto_variation(crypto_data)

        # Afficher les graphiques dans Streamlit (sans cette partie, les graphiques sont générés mais pas affichés)
        st.pyplot(Variation_fig)

        # Fermer la figure pour libérer la mémoire
        plt.close(Variation_fig)
