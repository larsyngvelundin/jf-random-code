import re
import json
import requests

api_key = ""
form_id = ""
submission_id = ""

url = f"https://api.jotform.com/inbox/form/{form_id}/submissions?checkSigns=1"
headers = {"apiKey": api_key, "referer": f"https://www.jotform.com/inbox/{form_id}"}

response = requests.get(url, headers=headers)
print(response.text)
if response.text.find("Cross-Site Requests") != -1:
    print("Response Content:", response.text)
else:
    submission_list = json.loads(response.text)["content"]
    print("Audit PDFs on this form:")
    for submission in submission_list:
        print(f"{submission['id']} : {submission['sealedFileURL']}")
