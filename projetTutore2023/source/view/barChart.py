import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import random


class BarChart:
    def __init__(self, liste_data):
        self.liste_crypto = liste_data

    # Méthode pour afficher le graphique de variation de la crypto-monnaie sélectionnée
    def _plot_crypto_variation(self, crypto):
        fig, ax = plt.subplots(figsize=(8, 6))
        variation_values = [crypto.percent_change_1h,
                            crypto.percent_change_24h, crypto.percent_change_7d]
        variation_labels = ["1h", "24h", "7 jours"]
        colors = ['#00a800' if value >=
                  0 else '#ff0000' for value in variation_values]

        ax.bar(variation_labels, variation_values, color=colors,
               width=0.3, edgecolor='#eaffea', linewidth=2)
        ax.set_xlabel('Temps', fontsize=12, fontweight='bold', color='#ffffff')
        ax.set_ylabel('Variations de la crypto-monnaie',
                      fontsize=12, fontweight='bold', color='#ffffff')
        ax.set_title(
            f'Variations de la crypto-monnaie {crypto.name}', fontsize=14, fontweight='bold', color='#ffffff')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.tick_params(colors='#ffffff')
        ax.set_facecolor('#333333')
        fig.patch.set_facecolor('#333333')
        # Ajouter une grille
        ax.grid(True, linestyle='--', linewidth=0.5, color='gray')
        for percent, value in enumerate(variation_values):
            # Arrondir à deux chiffres après la virgule
            rounded_value = round(value, 2)
            text_color = 'white'  # Couleur blanche pour les valeurs
            plt.text(percent, value, f"{rounded_value}", color=text_color,
                     ha='center', va='bottom', fontsize=10, fontweight='bold')

        plt.xticks(fontsize=10, fontweight='bold', color='#ffffff')
        plt.yticks(fontsize=10, fontweight='bold', color='#ffffff')
        plt.tight_layout()
        return fig
    # Méthode pour afficher les informations de la crypto-monnaie sélectionnée
    def afficher_crypto_info(self, selected_crypto_name):
        if not selected_crypto_name:
            st.warning("Veuillez sélectionner une crypto-monnaie")
            return

        # Chercher la crypto-monnaie sélectionnée dans la liste de données
        selected_crypto_data = [
            crypto for crypto in self.liste_crypto if crypto.name in selected_crypto_name]
        # style pour le texte
        st.markdown(f'''<style>
                        .cle {{
                            font-weight: bold;
                            font-size: 20px;
                            font-family: "Times New Roman", Times, serif;
                            color:#ffffff;
                        }}
                        .valeur {{
                            font-size: 20px;
                            font-family: Gill Sans, Monaco;
                            # font-style: italic;
                            color: #00ff00;
                            }}
                        </style>
                        ''', unsafe_allow_html=True)

        # Utiliser la classe BarChart pour afficher le graphique de variation de la crypto sélectionnée
        for crypto_data in selected_crypto_data:
            # affichage avec html/css
            st.markdown(f'''
                        <div style="elevation:16px; padding: 10px; border-top-left-radius: 10px; border-top-right-radius: 10px; background-color: #333333;">
                            <div style="background-color: rgb(51, 51, 51 ) ; border-radius: 2px; padding: 10px;">
                                <center>
                                <h3 style="font-family: 'Times New Roman', Times, serif; color: #ffffff;">
                                <img src="https://coinicons-api.vercel.app/api/icon/{crypto_data.symbol.lower()}" alt="{crypto_data.name}" width="34" height="34">
                                {crypto_data.name}
                                </h3>
                                </center>
                            </div>
                            <p> <span class="cle">Prix :</span> <span class="valeur">{round(crypto_data.price,2)}$ (USD)</span> </p>
                            <p> <span class="cle">Rang CMC :</span> <span class="valeur">{crypto_data.cmc_rank}</span></p>
                            <p> <span class="cle">Nombre de paires de marché :</span> <span class="valeur">{crypto_data.num_market_pairs}</span></p>
                            <p> <span class="cle">Volume 24h :</span> <span class="valeur">{crypto_data.volume_24h}</span></p>
                        </div>
                        ''', unsafe_allow_html=True)

            # Ajouter si vous le souhaitez...
            Variation_fig = self._plot_crypto_variation(crypto_data)

            # Afficher les graphiques dans Streamlit (sans cette partie, les graphiques sont générés mais pas affichés)
            st.pyplot(Variation_fig)

            # Fermer la figure pour libérer la mémoire
            plt.close(Variation_fig)

            # ligne de séparation
            st.markdown("""
                        <hr style="height:1.5px;border-width:0;color:black;background-color:black">
                        """, unsafe_allow_html=True)
            
    # Méthode pour afficher le graphique de comparaison des cryptomonnaies sélectionnées
    def afficher_courbe_comparative(self, selected_crypto):
        if not selected_crypto:
            cryptos = [crypto for crypto in self.liste_crypto]
            price_variation = [crypto.price for crypto in cryptos]
        else:
            # Données à afficher
            cryptos = [
                crypto for crypto in self.liste_crypto if crypto.name in selected_crypto]
            price_variation = [crypto.price for crypto in cryptos]

        # Créer l'axe x pour les catégories et définir la largeur des barres
        x = np.arange(cryptos.__len__())
        width = 0.4

        # Créer le diagramme en barres groupées pour chaque période
        fig, ax = plt.subplots(
            figsize=(cryptos.__len__()+9, (cryptos.__len__()/4)+8))

        # Generate a random color for each bar
        colors = [self.generate_bright_random_color()
                  for _ in range(len(cryptos))]
        bars = ax.bar(x - width/2, price_variation, width,
                      color=colors, edgecolor='white')

        # Ajouter des étiquettes et une légende
        ax.set_xlabel('Cryptomonnaies', fontsize=12, color='#ffffff')
        ax.set_ylabel('Variations prix', fontsize=12, color='#ffffff')
        ax.set_title(
            'Comparaison entre les prix des cryptomonnaies', color='#ffffff')

        # Incliner les étiquettes des crypto-monnaies de 45 degrés
        ax.set_xticks(x)
        ax.set_xticklabels((crypto.name for crypto in cryptos),
                           rotation=45, ha='right', fontsize=10, color='#ffffff')

        # Styling for the bars
        for i, bar in enumerate(bars):
            height = bar.get_height()
            ax.annotate(f'{height:.2f}$',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=13, color=bar.get_facecolor())

        # Hide the spines (the lines surrounding the plot)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.set_facecolor('#333333')
        fig.patch.set_facecolor('#333333')

        # Hide ticks
        ax.tick_params(axis='both', length=0, colors='white')

        # Show the plot
        plt.xticks(fontsize=10, fontweight='bold', color='white')
        plt.yticks(fontsize=10, fontweight='bold', color='white')
        plt.tight_layout()
        st.pyplot(fig)
        
    # Méthode pour générer une couleur aléatoire
    def generate_bright_random_color(self):
        # Generate random RGB values with higher intensity levels
        r = random.randint(100, 255)
        g = random.randint(100, 255)
        b = random.randint(100, 255)
        return f'#{r:02x}{g:02x}{b:02x}'
