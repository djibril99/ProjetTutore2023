import matplotlib.pyplot as plt

class BarChart:
    def __init__(self, cryptos):
        self.cryptos = cryptos
    
    def plot_crypto_variation(self, crypto):
        fig, ax = plt.subplots(figsize=(8, 6))
        variation_values = [crypto.percent_change_1h, crypto.percent_change_24h, crypto.percent_change_7d]
        variation_labels = ["1h", "24h", "7 jours"]
        colors = ['#00a800' if value >= 0 else '#ff0000' for value in variation_values]
        
        ax.bar(variation_labels, variation_values, color=colors, width=0.3, edgecolor='#eaffea', linewidth=2)
        ax.set_xlabel('Temps', fontsize=12, fontweight='bold', color='#ffffff')
        ax.set_ylabel('Variations de la crypto-monnaie', fontsize=12, fontweight='bold', color='#ffffff')
        ax.set_title(f'Variations de la crypto-monnaie {crypto.name}', fontsize=14, fontweight='bold', color='#ffffff')
        ax.spines['bottom'].set_color('#ffffff')
        ax.spines['left'].set_color('#ffffff')
        ax.tick_params(colors='#ffffff')
        ax.set_facecolor('#333333')
        fig.patch.set_facecolor('#333333')
        # Ajouter une grille
        ax.grid(True, linestyle='--', linewidth=0.5, color='gray')
        for percent, value in enumerate(variation_values):
            rounded_value = round(value, 2)  # Arrondir à deux chiffres après la virgule
            text_color = 'white'  # Couleur blanche pour les valeurs
            plt.text(percent, value, f"{rounded_value}", color=text_color, ha='center', va='bottom', fontsize=10, fontweight='bold')

        plt.xticks(fontsize=10, fontweight='bold', color='#ffffff')
        plt.yticks(fontsize=10, fontweight='bold', color='#ffffff')
        plt.tight_layout()

        return fig
