import json
import requests

URL = "https://swapi.dev/api/people/"

brownsData = dict()
for endpoint in range(1, 84):
    print("Information about: ", endpoint)
    if endpoint == 17:
        continue
    try:
        endpoint = str(endpoint)
        URL += endpoint + "/"
        peopleInfo = requests.get(URL).json()
        
        if peopleInfo["eye_color"] == "blue":
            brownsData[peopleInfo["name"]] = peopleInfo["eye_color"]
    except requests.exceptions.JSONDecodeError as message:
        print(message)
print(brownsData)

with open("eyedata.json", "w", encoding = "utf-8") as jsonFile:
    json.dump(brownsData, jsonFile, indent = 4)