import json
import os

import dotenv
import requests

dotenv.load_dotenv()
api_key = os.getenv("JOTFORM_API")

url = "https://api.jotform.com/user/forms?limit=5000"

headers = {
    "apiKey": api_key,
}

response = requests.get(url, headers=headers)
print("Status Code:", response.status_code)
if response.text.find("Cross-Site Requests") != -1:
    print("Response Content:", response.text)
elif response.status_code != 200:
    print(response.text)
else:
    forms = json.loads(response.text)

payment_gateways = {}
for form in forms["content"]:
    if "paymentProps" in form:
        gateway = form["paymentProps"]["gateway"]
        if gateway not in payment_gateways:
            payment_gateways[gateway] = []
        payment_gateways[gateway].append(form["id"])
print(payment_gateways)
