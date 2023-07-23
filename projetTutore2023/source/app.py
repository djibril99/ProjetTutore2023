# import streamlit as st
# import pandas as pd
# import requests

# # Récupérer votre clé API depuis votre compte CoinMarketCap
# API_KEY = 'ded5b890-0e71-41e4-b097-a3e73ec43f99'

# # URL de l'API CoinMarketCap
# API_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# # Paramètres de la requête API
# params = {
#     'start': '1',
#     'limit': '15',
#     'convert': 'USD'
# }

# # Entête de la requête avec la clé API
# headers = {
#     'Accepts': 'application/json',
#     'X-CMC_PRO_API_KEY': API_KEY
# }

# # Requête à l'API CoinMarketCap
# response = requests.get(API_URL, params=params, headers=headers)

# if response.status_code == 200:
#     data = response.json()
#     # Créer un DataFrame à partir des données
#     df = pd.DataFrame(data['data'])
# else:
#     st.write("Erreur lors de la récupération des données de l'API.")

# st.write("""# **:blue[Binance Price App]**
# A simple cryptocurrency price app pulling price data from *Binance API*.
# """, unsafe_allow_html=True, justify='center')


# st.header('**Selected Price**')

# # # Load market data from Binance API
# # df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

# # Custom function for rounding values
# def round_value(input_value):
#     if input_value.values > 1:
#         a = float(round(input_value, 2))
#     else:
#         a = float(round(input_value, 8))
#     return a

# col1, col2, col3 = st.columns(3)

# # Widget (Cryptocurrency selection box)
# col1_selection = st.sidebar.selectbox('Price 1', df.symbol, list(df.symbol).index("BTC") )
# # col2_selection = st.sidebar.selectbox('Price 2', df.symbol, list(df.symbol).index(2) )
# # col3_selection = st.sidebar.selectbox('Price 3', df.symbol, list(df.symbol).index(3) )
# # col4_selection = st.sidebar.selectbox('Price 4', df.symbol, list(df.symbol).index(4) )
# # col5_selection = st.sidebar.selectbox('Price 5', df.symbol, list(df.symbol).index(5) )
# # col6_selection = st.sidebar.selectbox('Price 6', df.symbol, list(df.symbol).index(6) )
# # col7_selection = st.sidebar.selectbox('Price 7', df.symbol, list(df.symbol).index(7) )
# # col8_selection = st.sidebar.selectbox('Price 8', df.symbol, list(df.symbol).index(8) )
# # col9_selection = st.sidebar.selectbox('Price 9', df.symbol, list(df.symbol).index(9) )

# # DataFrame of selected Cryptocurrency
# col1_df = df[df.symbol == col1_selection]
# # col2_df = df[df.symbol == col2_selection]
# # col3_df = df[df.symbol == col3_selection]
# # col4_df = df[df.symbol == col4_selection]
# # col5_df = df[df.symbol == col5_selection]
# # col6_df = df[df.symbol == col6_selection]
# # col7_df = df[df.symbol == col7_selection]
# # col8_df = df[df.symbol == col8_selection]
# # col9_df = df[df.symbol == col9_selection]

# # Apply a custom function to conditionally round values
# # col1_price = round_value(col1_df.weightedAvgPrice)
# # col2_price = round_value(col2_df.weightedAvgPrice)
# # col3_price = round_value(col3_df.weightedAvgPrice)
# # col4_price = round_value(col4_df.weightedAvgPrice)
# # col5_price = round_value(col5_df.weightedAvgPrice)
# # col6_price = round_value(col6_df.weightedAvgPrice)
# # col7_price = round_value(col7_df.weightedAvgPrice)
# # col8_price = round_value(col8_df.weightedAvgPrice)
# # col9_price = round_value(col9_df.weightedAvgPrice)

# # Select the priceChangePercent column
# # col1_percent = f'{float(col1_df.priceChangePercent)}%'
# # col2_percent = f'{float(col2_df.priceChangePercent)}%'
# # col3_percent = f'{float(col3_df.priceChangePercent)}%'
# # col4_percent = f'{float(col4_df.priceChangePercent)}%'
# # col5_percent = f'{float(col5_df.priceChangePercent)}%'
# # col6_percent = f'{float(col6_df.priceChangePercent)}%'
# # col7_percent = f'{float(col7_df.priceChangePercent)}%'
# # col8_percent = f'{float(col8_df.priceChangePercent)}%'
# # col9_percent = f'{float(col9_df.priceChangePercent)}%'

# # Create a metrics price box
# # col1.metric(col1_selection)
# # col2.metric(col2_selection, col2_price, col2_percent)
# # col3.metric(col3_selection, col3_price, col3_percent)
# # col1.metric(col4_selection, col4_price, col4_percent)
# # col2.metric(col5_selection, col5_price, col5_percent)
# # col3.metric(col6_selection, col6_price, col6_percent)
# # col1.metric(col7_selection, col7_price, col7_percent)
# # col2.metric(col8_selection, col8_price, col8_percent)
# # col3.metric(col9_selection, col9_price, col9_percent)

# st.header('**All Price**')
# st.dataframe(df)
# # st.area_chart  (df. ) 
# st.info('Credit: Created by Chanin Nantasenamat (aka [Data Professor](https://youtube.com/dataprofessor/))')

# st.markdown("""
# <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
# <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
# <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
# """, unsafe_allow_html=True)#



#-------------------

# import streamlit as st
# import pandas as pd
# import requests

# # Récupérer votre clé API depuis votre compte CoinMarketCap
# API_KEY = 'ded5b890-0e71-41e4-b097-a3e73ec43f99'

# # URL de l'API CoinMarketCap
# API_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# # Paramètres de la requête API
# params = {
#     'start': '1',
#     'limit': '50',
#     'convert': 'EUR',
#     # 'sort': 'name'
# }

# # Entête de la requête avec la clé API
# headers = {
#     'Accepts': 'application/json',
#     'X-CMC_PRO_API_KEY': API_KEY
# }

# # Requête à l'API CoinMarketCap
# response = requests.get(API_URL, params=params, headers=headers)

# # Vérifier si la requête a réussi
# if response.status_code == 200:
#     data = response.json()
#     # Créer un DataFrame à partir des données
#     df = pd.DataFrame(data['data'])
#     # Extraire les colonnes nécessaires
#     df = df[['symbol', 'name', 'quote']]
#     df['price'] = df['quote'].apply(lambda x: x['EUR']['price'])
#     df = df[['symbol', 'name', 'price']]
#     # Afficher les informations des cryptomonnaies dans une table
#     st.table(df)
    
# else:
#     st.write("Erreur lors de la récupération des données de l'API.")

#-------------------
# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import requests
# from PIL import Image

# url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# params = {
#   'start':'1',
#   'limit':'50',
#   'convert':'USD'
# }
# headers = {
#   'Accepts': 'application/json',
#   'X-CMC_PRO_API_KEY': 'ded5b890-0e71-41e4-b097-a3e73ec43f99',
# }

# response = requests.get(url, headers=headers, params=params)
# data = response.json()

# df = pd.DataFrame(data)
# # df = df[['name', 'quote', 'symbol']]
# # df['icon'] = df['symbol'].apply(lambda x: f"https://s2.coinmarketcap.com/static/img/coins/64x64/{x}.png")

# # st.title('Visualisation des variations de cryptomonnaie')

# # # Afficher les icônes
# # for index, row in df.iterrows():
# #     # icon = Image.open(requests.get(row['icon'], stream=True).raw)
# #     # st.image(icon, use_column_width=True)
# #     st.write(row['name'])
# #     #afficher image de la crypto
# #     st.image(f"https://s2.coinmarketcap.com/static/img/coins/64x64/{index+1}.png", width=25)

# # # Afficher le graphique
# # fig, ax = plt.subplots()
# # df['quote'].apply(lambda x: pd.Series(x['USD'])).plot(ax=ax)
# # st.pyplot(fig)

# # Convertir les colonnes numériques en types appropriés
# numeric_columns = ['price_usd', 'market_cap_usd', 'percent_change_24h']
# df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric)

# # Afficher les données dans l'application
# st.title("Visualisation des variations de cryptomonnaies")
# st.dataframe(df)

# # Tracer un graphique des variations de prix
# plt.figure(figsize=(10, 5))
# plt.plot(df['name'], df['percent_change_24h'], marker='o')
# plt.xlabel('Cryptomonnaie')
# plt.ylabel('Variation en % (24h)')
# plt.xticks(rotation=45)
# st.pyplot(plt)
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
params = {
  'start':'1',
  'limit':'15',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'ded5b890-0e71-41e4-b097-a3e73ec43f99',
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
# Obtenir les données
coin_data = data

# # Créer un DataFrame avec les données
df = pd.DataFrame(coin_data['data'])

# Créer un DataFrame avec les données du crypto 'BTC'
# df = pd.DataFrame([coin for coin in coin_data['data'] if coin['symbol'] == 'BTC'])


# # Convertir les colonnes numériques en types appropriés
# numeric_columns = ['price_usd', 'market_cap_usd', 'percent_change_24h']
# df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric)

# # Afficher les le nom et le symbol dans l'application
st.title("Visualisation des variations de cryptomonnaies")
st.dataframe(df)
# # Tracer un graphique des variations de prix
plt.rcParams['text.color'] = 'red'

plt.figure(figsize=(3, 3),
          facecolor='darkgray',
           )
# df['name'], df['quote']
df['percent_change_1h'] = df['quote'].apply(lambda x: x['USD']['percent_change_1h'])
df['volume_24h'] = df['quote'].apply(lambda x: x['USD']['volume_24h'])
plt.plot(df['name'], df['percent_change_1h'])
plt.xlabel('Cryptomonnaie')
st._arrow_line_chart(df['volume_24h'])

# plt.ylabel('volume en  % (24h)')
# plt.xticks(rotation=90)
# for i, value in enumerate(df['percent_change_1h']):
#     rounded_value = round(value, 2)  # Arrondir à deux chiffres après la virgule
#     plt.text(i, value, f"{rounded_value}", color='blue', ha='center')
# st.pyplot(plt)