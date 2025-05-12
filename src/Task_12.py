import requests as re

date = '2025-05-02'
response = re.get('https://api.nbp.pl/api/cenyzlota/' + '2025-05-02' + '?format=json')
json = response.json()
print(json)

