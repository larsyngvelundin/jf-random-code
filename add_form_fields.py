import requests
from time import sleep

api_key = ""

form_id = ""


headers = {"apiKey": api_key}
url = f"https://api.jotform.com/form/{form_id}/questions"


for i in range(0, 100):
    sleep(1)
    payload = {
        "question[type]": "control_textarea",
        "question[order]": i + 3,
        "question[rows]": "163",
        "question[text]": f"Long field #{i + 1}",
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
