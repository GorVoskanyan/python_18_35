import json
import requests

BASEURL = "https://swapi.dev/api/people/"

eyeData = dict()

for endpoint in range(1, 84):
    print("Information about: ", endpoint)
    
    if endpoint == 17:
        continue
    
    try:
        URL = BASEURL + str(endpoint) + "/"
        response = requests.get(URL)

        peopleInfo = response.json()
        
        if peopleInfo["eye_color"] == "yellow":
            eyeData[peopleInfo["name"]] = peopleInfo["eye_color"]
            
    except requests.exceptions.JSONDecodeError as message:
        print(message)
    except json.decoder.JSONDecodeError as message:
        print(message)

print(eyeData)
with open("eyedata.json", "w", encoding = "utf-8") as jsonFile:
    json.dump(eyeData, jsonFile, indent = 4)
