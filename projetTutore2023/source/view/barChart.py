import matplotlib.pyplot as plt
import streamlit as st

class BarChart:
    def __init__(self, liste_data):
        self.liste_cripto  = liste_data
        
    def _plot_crypto_variation(self, crypto):
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
    
    def afficher_crypto_info(self,selected_crypto_name):
        if not selected_crypto_name:
            st.warning("Veuillez sélectionner une crypto-monnaie")
            return

        # Chercher la crypto-monnaie sélectionnée dans la liste de données
        selected_crypto_data = [crypto for crypto in self.liste_cripto if crypto.name in selected_crypto_name]

        if not selected_crypto_data:
            st.warning("Aucune crypto-monnaie correspondante trouvée")
            return

        # Utiliser la classe BarChart pour afficher le graphique de variation de la crypto sélectionnée
        for crypto_data in selected_crypto_data:
            # Afficher les informations de la crypto sélectionnée
            st.write('Nom :', crypto_data.name)
            st.write('Prix :', crypto_data.price)
            st.write('Rang CMC :', crypto_data.cmc_rank)
            st.write('Nombre de paires de marché :', crypto_data.num_market_pairs)
            st.write('Volume 24h :', crypto_data.volume_24h)
             # Ajouter si vous le souhaitez...
            Variation_fig = self._plot_crypto_variation(crypto_data)

            # Afficher les graphiques dans Streamlit (sans cette partie, les graphiques sont générés mais pas affichés)
            st.pyplot(Variation_fig)

            # Fermer la figure pour libérer la mémoire
            plt.close(Variation_fig)

