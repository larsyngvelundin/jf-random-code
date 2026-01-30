import requests
import json
from time import sleep

apiKey = ""
formID = ""

headers = {"apiKey": apiKey}


options = ["", "", ""]


for i in range(1, 73):
    for j in range(0, len(options)):
        options[j] += f"f{i}o{j}|"

print(options[0][:-1])

fields = ["126", "127", "128"]

for i in range(0, 3):
    payload = {
        "question[calcValues]": options[i][:-1],
        "question[options]": options[i][:-1],
    }
    postUrl = f"https://api.jotform.com/form/{formID}/question/{fields[i]}"
    response = requests.request("POST", postUrl, headers=headers, data=payload)
    print(response.text)
    sleep(1)
