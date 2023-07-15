import matplotlib.pyplot as plt

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

