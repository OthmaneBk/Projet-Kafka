def statics(stock_data, symbol):
    # Afficher des statistiques simples pour chaque symbole
        if len(stock_data[symbol]) > 1:
            prices = [item['price'] for item in stock_data[symbol]]
            avg_price = sum(prices) / len(prices)
            min_price = min(prices)
            max_price = max(prices)
            
            print(f"Statistiques pour {symbol}: Moyenne={avg_price:.2f}, Min={min_price:.2f}, Max={max_price:.2f}")
            print("-" * 50)