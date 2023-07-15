import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class BarChart:
    def __init__(self, cryptos):
        self.cryptos = cryptos

    def plot_prices(self):
        noms = []
        prix = []

        for crypto in self.cryptos:
            noms.append(crypto.name)
            prix.append(crypto.price)

        plt.figure(figsize=(10, 6))
        plt.bar(noms, prix)
        plt.xlabel('Crypto-monnaie')
        plt.ylabel('Prix')
        plt.title('Prix des crypto-monnaies')
        plt.xticks(rotation=45)

        return plt  # Retourne l'objet plt
    
    def plot_variation_1h(self, crypto):
        fig, ax = plt.subplots(figsize=(10, 6))
        # bon j'explique: cette ligne trace le digramme la j'ai donné le nom en abscisse et la chagement en ordonné
        ax.bar(crypto.name, crypto.percent_change_1h)
        ax.set_xlabel('Crypto-monnaie')
        ax.set_ylabel('Variation en 1 heure (%)')
        ax.set_title('Variation en 1 heure des crypto-monnaies')
        ax.tick_params(axis='x', rotation=45)

        return fig

    def plot_variation_24h(self, crypto):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(crypto.name, crypto.percent_change_24h)
        ax.set_xlabel('Crypto-monnaie')
        ax.set_ylabel('Variation en 24 heures (%)')
        ax.set_title('Variation en 24 heures des crypto-monnaies')
        ax.tick_params(axis='x', rotation=45)