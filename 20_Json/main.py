# Java Script Object Notation

import json

import requests

URL = 'https://swapi.dev/api/people/'

peoples_data = dict()

for endpoint in range(1, 84):
    print('Fetching info about people:', endpoint)
    if endpoint == 17:
        continue

    try:
        endpoint = str(endpoint)
        URL += endpoint + '/'
        people_info = requests.get(URL).json()

        if people_info['hair_color'] == 'blond':
            peoples_data[people_info['name']] = people_info['hair_color']
    except requests.exceptions.JSONDecodeError:
        print('Something went wrong...')

print(peoples_data)
with open('peoples_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(peoples_data, json_file)


# response = requests.get(URL)
# if response.status_code == 200:
    # print(type(response.text))
    # data = response.text
    # print(type(data))
    # data = json.loads(data)
    # print(type(data))
    # data = json.dumps(data)
    # print(type(data))

    # data = response.json()
    # print(data)
    # print(type(data))

    # with open('data.json', 'w', encoding='utf-8') as json_file:
    #     json.dump(data, json_file, indent=4)


# with open('data.json', 'r', encoding='utf-8') as json_file:
#     data = json.load(json_file)

# print(data)
# print(type(data))
