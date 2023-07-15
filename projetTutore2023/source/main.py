import streamlit as st
from model.DataReader import DataReader
from model.AfficherCrypto import afficher_crypto_info

# Ajouter un titre à l'application
st.title("Bienvenue sur Crypto4Fantastic")

# Récupérer les données depuis le lien
data_reader = DataReader()
liste_data = data_reader.get_data()

if len(liste_data) == 0:
        st.error('Error while loading data')
        st.stop()
else:
        # Affiche le message  au-dessus du select
        st.subheader('Veuillez choisir une crypto-monnaie')

        # Créer une liste déroulante pour sélectionner la crypto-monnaie de notre choix 
        crypto_names = [crypto.name for crypto in liste_data]
        selected_crypto = st.selectbox('Sélectionner une crypto-monnaie', crypto_names)

        # Afficher le bouton "Valider"
        if st.button('Valider'):
                # Redirection vers la page d'affichage de la crypto-monnaie sélectionnée
                afficher_crypto_info(selected_crypto, liste_data)
