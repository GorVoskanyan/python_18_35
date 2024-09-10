import json
import requests


URL = 'https://swapi.dev/api/people/'

   
peoples_data = dict()

for endpoint in range(1,82):
    print('Fetching info about people:',endpoint)
    if endpoint == 17:
        continue


    endpoint = str(endpoint)
    response = requests.get(URL +endpoint + '/')
    data = json.loads(response.text)

    if data['skin_color'] == 'fair':
        peoples_data[data['name']] = data['skin_color']

    
print(peoples_data)   

with open('data.json','w',encoding = 'utf-8') as json_file:
    json.dump(peoples_data,json_file,indent = 4)