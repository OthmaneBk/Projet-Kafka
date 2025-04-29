from consumer import  consumer
import pandas as pd
from datetime import datetime
from statics import statics
from saveData import saveData

if __name__=='__main__':
    # Dictionnaire pour stocker les derniers prix par symbole
    stock_data = {}

    try:
        print("Démarrage du consommateur Kafka. Appuyez sur Ctrl+C pour arrêter.")
        
        # Boucle pour consommer les messages
        for message in consumer:
            data = message.value
            
            # Extraire les données du message
            symbol = data.get('symbol')
            price = data.get('price')
            timestamp = data.get('timestamp')
            
            # Convertir le timestamp en format lisible
            readable_time = datetime.fromtimestamp(timestamp/1000).strftime('%Y-%m-%d %H:%M:%S')
            
            # Stocker les données dans notre dictionnaire
            if symbol not in stock_data:
                stock_data[symbol] = []
            
            stock_data[symbol].append({
                'price': price,
                'timestamp': timestamp,
                'readable_time': readable_time
            })
            statics(stock_data, symbol)  # Appeler la fonction de statistiques pour chaque symbole

    except KeyboardInterrupt:
        # Gérer l'arrêt propre du programme
        print("Arrêt du consommateur Kafka")
        
        # Créer un DataFrame avec toutes les données collectées et l'enregistrer
        if stock_data:
            all_data = []
            for symbol, data_points in stock_data.items():
                for point in data_points:
                    all_data.append({
                        'symbol': symbol,
                        'price': point['price'],
                        'timestamp': point['timestamp'],
                        'readable_time': point['readable_time']
                    })
            
            df = pd.DataFrame(all_data)
            saveData(df)  # Appeler la fonction pour sauvegarder les données
        
    finally:
        # Fermer le consommateur
        consumer.close()
        print("Consommateur fermé")