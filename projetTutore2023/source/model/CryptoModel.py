class CryptoModel:
        def __init__(self) :

                #declarrer les attributs de l'objet dont on aura besoin
                #ces derniers doivent etre les memes que les cles du dictionnaire json recupere depuis l'api 
                #declarrer les attributs de l'objet dont on aura besoin  
                self.price = 0
                self.name = ''
                self.symbol = ''
                self.cmc_rank = 0
                self.num_market_pairs = 0
                self.volume_24h = 0
                self.percent_change_1h = 0
                self.percent_change_24h = 0
                self.percent_change_7d = 0
                
                
      
        def load(self, data):
                #hydrater l'objet avec les donnees recuperees depuis l'api
                #data est un dictionnaire et les cles sont les noms des attributs
                # pour traduis ls donnees de cette objet en format json on utilise la fonction dumps de json sur l'objet en question
                if not isinstance(data, dict):
                        return
                #self.timestamp = data['timestamp']
                #pour traduire les donne
                for key, value in data.items():
                        self._charge(key, value)
                        
        
        #utiliser la recursivité pour charger les donnees de l'objet
        #verifier si la valeur est un dictionnaire et si oui appeler la fonction load pour charger les donnees de ce dictionnaire
        def _charge(self,key , value):
                #verifier si c est un dict
                if isinstance(value, dict):
                        self.load(value)
                else:
                        #verifier si l'attribut existe
                        if hasattr(self, key):
                                setattr(self,key,value)
                                
        
        
        #methode de classe pour convertir les donnees en format json pour pouvoir les afficher dans un dataframe correctement
        @classmethod
        def data_array_to_json(cls, tableau_donnee:list):
                data_json = {}
                #recuperer les attritus de la classe CryptoModel et les ajouter dans le dictionnaire comme des cles 
                listeKeys = [key for key in CryptoModel().__dict__]
                
                #creer une liste vide pour chaque cle , la cle represente le nom de la colonne et la liste represente les donnees de la colonne
                for key in listeKeys:
                        data_json[key] = []
                        
                #ajouter les donnees de chaque colonne du tableau 
                for crypto_data in tableau_donnee:
                        dict_crypto = crypto_data.__dict__
                        for key in listeKeys:
                                data_json[key].append(dict_crypto[key])
                
                return data_json