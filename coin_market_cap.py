# API do Coin Market Cap (https://coinmarketcap.com/api/documentation/v1/)
# Gerar API Key ((secrets.py)

#Importação de módulos e API key
import requests
import secrets

#Fazendo uma request
#Precisamos sabe o que é necessário para realizar uma request
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': secrets.API_KEY,
}

r = requests.get(url, headers=headers)

#print(r.status_code) #status code da requisição 200 => OK
#print(r.json()) #retorna um dicionário com o resultado da requisição

#Tornado o json legível
# from pprint import pprint as pp

# p = pp(r.json()['data'][0]) #[0]bitcoin [1]litecoin

# print(p)


#Contruindo uma classe para fazermos chamadas a API
