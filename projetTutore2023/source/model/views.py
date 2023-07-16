import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

from model.DataReader import DataReader
from model.CryptoModel import CryptoModel

class DataVisualizer:
    def __init__(self):
        self.data_reader = DataReader()

    def run(self):
        # Get the data from the API
        liste_data = self.data_reader.get_data()

        if len(liste_data) == 0:
            st.error('Error while loading data')
            st.stop()

        # Set up the sidebar inputs
        st.title("Visualisation des données cryptomonnaie")
        ticker = st.sidebar.text_input('Search')
        start_date = st.sidebar.date_input('Start date')
        end_date = st.sidebar.date_input('End Date')

        # Create a DataFrame from the data
        df = pd.DataFrame(CryptoModel.data_array_to_json(liste_data))

        x = st.dataframe(df)
        print(type(liste_data[1].__dict__['percent_change_1h']))

        # Convert the relevant columns to datetime format
        df['last_updated'] = pd.to_datetime(df['last_updated']).dt.date

        # Filter the data based on the selected dates
        df = df[(df['last_updated'] >= start_date) & (df['last_updated'] <= end_date)]

        # Plot the histogram
        fig, ax = plt.subplots()
        ax.hist(df['price'], bins=10)  # Adjust the number of bins as needed
        ax.hist(df['price'], bins=20)  # Adjust the number of bins as needed

        ax.set_xlabel('Price')
        ax.set_ylabel('Frequency')
        ax.set_title('Distribution of Cryptocurrency Prices')
        plt.tight_layout()

        # Disable the warning
        st.set_option('deprecation.showPyplotGlobalUse', False)

        # Show the graph in Streamlit
        st.pyplot(fig)
