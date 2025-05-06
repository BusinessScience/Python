import requests as r

response = r.get('https://api.nbp.pl/api/exchangerates/rates/c/usd/2025-05-02?format=json')
json = response.json()
print(json['rates'][0]['bid'])