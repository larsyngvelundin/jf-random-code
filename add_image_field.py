import requests

api_key = ""
form_id = ""
logo_url = ""

headers = {"apiKey": api_key}
url = f"https://api.jotform.com/form/{form_id}/questions"

payload = {
    "question[type]": "control_image",
    "question[src]": logo_url,
    "question[order]": 1,
    "question[width]": 140,
    "question[height]": 140,
}
response = requests.request("POST", url, headers=headers, data=payload)
