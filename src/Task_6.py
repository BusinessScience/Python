from http.client import responses

import requests as r

response = r.get('https://api.nbp.pl/api/cenyzlota/2025-05-02?format=json')
#print(response.text)
json = response.json()
print(json)
print(type(json))