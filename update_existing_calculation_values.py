import requests
import json
from time import sleep

apiKey = ""
formID = ""

headers = {"apiKey": apiKey}

url = f"https://api.jotform.com/form/{formID}/questions"
response = requests.request("GET", url, headers=headers)
questionData = json.loads(response.text)["content"]

for key in questionData:
    if questionData[key]["type"] == "control_radio":
        if "calcValues" in questionData[key] and "options" in questionData[key]:
            print(key, end="")
            calcValues = questionData[key]["options"]
            calcValues = calcValues.replace("Not at all", "0")
            calcValues = calcValues.replace("Somewhat", "1")
            calcValues = calcValues.replace("Absolutely", "2")
            calcValues = calcValues.split("|")
            prefix = questionData[key]["text"]
            prefix = prefix[0 : prefix.find(".")]
            newCalcValues = f"f{prefix}o{calcValues[0]}|f{prefix}o{calcValues[1]}|f{prefix}o{calcValues[2]}"
            print(f" - {calcValues}")
            print(f" - {newCalcValues}")
            payload = {"question[calcValues]": newCalcValues}
            postUrl = f"https://api.jotform.com/form/{formID}/question/{key}"
            response = requests.request("POST", postUrl, headers=headers, data=payload)
            print(response.text)
            sleep(1)
