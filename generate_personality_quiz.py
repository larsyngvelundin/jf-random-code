import requests
import json
from time import sleep

apiKey = ""
formID = ""

headers = {"apiKey": apiKey}

colAnswers = [
    "null",
    "EB",
    "GA",
    "CD",
    "HI",
    "FE",
    "BA",
    "GD",
    "FH",
    "CI",
    "EA",
    "HG",
    "BD",
    "FC",
    "EI",
    "HD",
    "BG",
    "AF",
    "CE",
    "BI",
    "FD",
    "GC",
    "HA",
    "BF",
    "IG",
    "ED",
    "AI",
    "BC",
    "HE",
    "GF",
    "ID",
    "AC",
    "HB",
    "EG",
    "AD",
    "IF",
    "CH",
]

letToNum = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8}

options = ["", "", "", "", "", "", "", "", ""]


for i in range(1, len(colAnswers)):
    for j in range(0, 2):
        options[letToNum[colAnswers[i][j]]] += (
            f"{colAnswers[i][j]}{i}{colAnswers[i][j]}|"
        )

print(options[0][:-1])


fields = {
    "A": "144",
    "B": "145",
    "C": "146",
    "D": "147",
    "E": "148",
    "F": "149",
    "G": "150",
    "H": "151",
    "I": "152",
}

for i in range(0, len(options)):
    payload = {
        "question[calcValues]": options[i][:-1],
        "question[options]": options[i][:-1],
    }
    postUrl = f"https://api.jotform.com/form/{formID}/question/{fields[options[i][0]]}"
    response = requests.request("POST", postUrl, headers=headers, data=payload)
    print(response.text)
    sleep(1)
