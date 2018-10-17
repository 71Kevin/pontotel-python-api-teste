import requests
import json

req = None
sair = False
while sair == False:
   try:
      req = requests.get('http://www.omdbapi.com/?apikey=5d9cabe3&t=' + input('\nInforme o nome do filme (exemplo: Frozen): '))
      dicionario = json.loads(req.text)
      print(dicionario)
   except:
      print('Erro na conexão ou limite de request atingido')
      exit()
