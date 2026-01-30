import re
import json
import requests

api_key = ""
form_id = ""

headers = {"apiKey": api_key}
url = f"https://api.jotform.com/form/{form_id}/properties"
response = requests.request("GET", url, headers=headers)
form_properties = json.loads(response.text)
conditions = form_properties["content"]["conditions"]
condition_text = json.dumps(conditions)
# print(len(condition_text))


def find_emails_in_string(s):
    email_pattern = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
    emails = re.findall(email_pattern, s)
    return emails


found_emails = find_emails_in_string(condition_text)
for email in found_emails:
    print(email)
