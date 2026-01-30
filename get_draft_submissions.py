import json
import re
import requests

api_key = ""
form_id = ""

url = f"https://www.jotform.com/API/sheets/{form_id}/sheet/{form_id}/view/{form_id}/details?next5=1"

headers = {
    "apiKey": api_key,
    "referer": f"https://www.jotform.com/tables/{form_id}",
    "host": "www.jotform.com",
}
# print(url)
response = requests.get(url, headers=headers)
if response.text.find("Cross-Site Requests") != -1:
    print("Response Content:", response.text)
else:
    draft_list = json.loads(response.text)["content"]["incompleteSubmissions"]
    print("Drafts on this form:")
    print(draft_list)
    for i in range(0, len(draft_list)):
        print(draft_list[i])
        draft_link = f"https://www.jotform.com/draft/{draft_list[i]['saclID']}"
