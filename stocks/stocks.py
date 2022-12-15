import requests
from datetime import datetime

print(datetime.now())

def get_current_price(stock):
    session = requests.session()
    session.headers.update({"Accept": "application/json",
                                "User-Agent": "finnhub/python"})
    session.params["token"] = "ced22u2ad3i8too9noh0ced22u2ad3i8too9nohg"
    response = getattr(session, "get")("https://finnhub.io/api/v1/quote", params={"symbol": stock})
    return datetime.now(), response.json()["c"]

date, current_price = get_current_price("AAPL")
with open('/Users/ssotomayorba/Documents/Personal/projects/fincrypstocks/data/stock_data.csv', 'a') as file:
    file.write(str(date) + "," + str(current_price)+ "\n")