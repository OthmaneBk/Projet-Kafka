
def saveData(df):
    df.to_csv('stock_prices.csv', index=False)
    print(f"Données sauvegardées dans stock_prices.csv")