import requests
from datetime import datetime

def get_current_price(crypto):

    headers = {
        "X-CMC_PRO_API_KEY" : "c6c41791-1913-42f2-977d-ef13f907799c",
        'Accepts' : 'application/json'
    }
    params = {
        "symbol": crypto,
        "convert": "USD"
    }
    crypto_data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest", params=params, headers=headers).json()
    return datetime.now(), crypto_data["data"][crypto]["quote"]["USD"]["price"]

date, current_price = get_current_price("BTC")
with open('/Users/ssotomayorba/Documents/Personal/projects/fincrypstocks/data/crypto_data.csv', 'a') as file:
    file.write(str(date) + "," + str(current_price)+ "\n")
