import requests
from random import randint
from time import sleep


form_id = ""
question_id1 = ""
question_id2 = ""
api_key = ""
amount_of_subs = 100


url = f"https://api.jotform.com/form/{form_id}/submissions?apiKey={api_key}"


for i in range(0, amount_of_subs):
    payload = {
        f"submission[{question_id1}]": f"4{randint(0, 9)}.{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}, 1{randint(0, 9)}.{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}",
        f"submission[{question_id2}]": f"{i}-{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}",
    }

    files = []
    headers = {"Cookie": ""}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)
    sleep(0.01)
