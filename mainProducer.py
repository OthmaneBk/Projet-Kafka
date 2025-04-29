import random 
import time 
from SymboleBoursier import stocks
from producer import producer


if __name__ == "__main__":
    # Fonction pour produire les cours des actions 
    def produce_stock_prices (): 
        while True : 
            for stock in stocks: 
                price = round (random.uniform( 100 , 500 ), 2 ) 
                timestamp = int ( round (time.time() * 1000 )) 
                message = { 'symbol' : stock, 'price' : price, 'timestamp' : timestamp} 
                producer.send( 'topic-stock-prices' , value=message) 
                print ( f"Envoyé : {message} " ) 
            time.sleep( 1 ) 

    produce_stock_prices()