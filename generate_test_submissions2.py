import json
import os
from time import sleep
import dotenv
import requests
import randomnames.random_names as rn

dotenv.load_dotenv()
api_key = os.getenv("JOTFORM_API")

form_id = ""

url = f"https://api.jotform.com/form/{form_id}/submissions"

headers = {
    "apiKey": api_key,
}

for i in range(0, 50):
    payload = {
        "submission[3][first]": rn.First(),
        "submission[3][last]": rn.Last(),
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    sleep(0.01)
