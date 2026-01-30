import json
import re
import requests

api_key = ""
form_id = ""

url = f"https://www.jotform.com/API/sheets/{form_id}/user/pendingpayments?filter={{%22formIDs%22:%20[%22{form_id}%22]}}&limit=1000&sheets=1"

headers = {
    "apiKey": api_key,
    "referer": f"https://www.jotform.com/tables/{form_id}",
    "host": "www.jotform.com",
}
response = requests.get(url, headers=headers)
if response.text.find("Cross-Site Requests") != -1:
    print("Response Content:", response.text)
else:
    draft_list = json.loads(response.text)["content"]
    print("Drafts on this form:")
    print(draft_list)
    for item in draft_list:
        print(item["id"])
