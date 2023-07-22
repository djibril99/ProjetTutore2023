import streamlit as st
from model.DataReader import DataReader
from view.barChart import BarChart
from model.DataReader import DataReader
import base64

# Ajouter un titre à l'application
def get_img_as_base64(file):
        with open(file, "rb") as f:
                data = f. read ( )
        return base64.b64encode (data) . decode ()
img = get_img_as_base64 ("../source/red.jpg")
st.markdown(f'''
    <style>
      .container {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
        width: 100%;
        background-color: #2f3131ba;
        margin-bottom: 15px;
        border-radius: 15px;
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.5); /* White shadow effect */
        transition: box-shadow 0.3s ease; /* Add transition effect for box-shadow */
      }}
      .container:hover {{
        box-shadow: 0 0 40px rgba(255, 255, 255, 0.8); /* Adjust the shadow on hover */
      }}
      .animated-text {{
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 0.5em;
        display: inline-block;
        padding: 1.5em 0em;
        font-weight: bolder;
        width: 50em;
      }}
      .spans {{
        font: 900 2em/1 "Oswald";
        letter-spacing: 0;
        display: block;
        text-shadow: 0 0 50px rgba(255, 255, 255, 0.5);
        background: url("data:image/png;base64,{img}") repeat-y;
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        -webkit-animation: aitf 100s linear infinite;
        -webkit-transform: translate3d(0, 0, 0);
        -webkit-backface-visibility: hidden;
      }}
      /* Animate Background Image */
      @-webkit-keyframes aitf {{
        0% {{
          background-position: 0% 50%;
        }}
        100% {{
          background-position: 100% 50%;
        }}
      }}
    </style>

    <div class="container">
      <p class="animated-text">
        <span class="spans">
          Bienvenue sur Crypto4Fantastic
        </span>
      </p>
    </div> 
''', unsafe_allow_html=True)

# Récupérer les données depuis le lien
data_reader = DataReader(st.slider('Nombre de cryptomonnaies à afficher', 1, 100, 10))
liste_data = data_reader.get_data()
print(data_reader.limit)

# Afficher un message d'erreur si les données n'ont pas été récupérées
            

if len(liste_data) == 0:
        st.error('Error while loading data')
        st.stop()
else:
        # Affiche le message  au-dessus du select
        st.subheader('Veuillez choisir une crypto-monnaie')

        # changer la limite des cryptos à afficher
        
        # Créer une liste déroulante pour sélectionner la crypto-monnaie de notre choix 
        crypto_names = [crypto.name for crypto in liste_data]
        selected_crypto= st.multiselect('Sélectionner au moins une crypto-monnaie', crypto_names)
        
        col1 , col2 = st.columns(2)
        with col1 :
                # Afficher le bouton "Valider"
                bnt_click = st.button(
                        label='Afficher la variation des cryptomonnaies')
        with col2 :
                # Afficher le bouton "Comparer"
                bnt_click2 = st.button(
                        label='Comparer le prix des cryptomonnaies')
        if bnt_click:
                barChart =  BarChart(liste_data)
                barChart.afficher_crypto_info(selected_crypto)
        elif bnt_click2:
                barChart =  BarChart(liste_data)
                barChart.afficher_courbe_comparative(selected_crypto)

