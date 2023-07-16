# from requests import Request, Session
# from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
# import json
# import streamlit as st
# import pandas as pd


# url = 'url = https://pro-api.coinmarketcap.com/v2/cryptocurrency/info/slug=bitcoin'
# # parameters = {
# #   'start':'1',
# #   'limit':'5000',
# #   'convert':'USD'
# # }
# headers = {
#   'Accepts': 'application/json',
#   'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
# }

# session = Session()
# session.headers.update(headers)

# try:
#   response = session.get(url)
#   data = json.loads(response.text)
#   print(data)
# except (ConnectionError, Timeout, TooManyRedirects) as e:
#   print(e)
  
  
# # df = pd.DataFrame({'Colonne 1': [1, 2, 3],
# #                    'Colonne 2': ['a', 'b', 'c']})
# # st.dataframe(df)
import requests
import streamlit as st

# URL de l'API et clé API
url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/info"
api_key = "b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c"

# Paramètres de la requête GET
params = {
    "id": "1",  # ID de la crypto-monnaie (à spécifier)
}

# Effectuer la requête GET avec les paramètres et l'API key
response = requests.get(url, headers={"X-CMC_PRO_API_KEY": api_key}, params=params)

# Vérifier si la requête a réussi
if response.status_code == 200:
    data = response.json()
    crypto_data = data["data"]

    # Parcourir les données de chaque crypto-monnaie
    for crypto in crypto_data.values():
        name = crypto["name"]
        logo_url = crypto["logo"]

        # Afficher le nom de la crypto-monnaie
        st.write(f"Nom : {name}")

        # Afficher l'image du logo de la crypto-monnaie
        image = requests.get(logo_url).content
        st.image(image, use_column_width=True)
