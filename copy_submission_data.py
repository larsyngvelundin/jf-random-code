import json
import requests
from random import randint
from time import sleep

submission_id = ""
form_id = ""
api_key = ""
files = []
headers = {"apiKey": api_key}

# Fetching an existing submission as an example:
url = f"https://api.jotform.com/submission/{submission_id}"


submission_response = requests.get(url, headers=headers)
submission_data = json.loads(submission_response.text)
submission_answers = submission_data["content"]["answers"]

print(submission_answers["3"]["answer"])
print(submission_answers["4"]["answer"])
print(submission_answers["5"]["answer"])
print(submission_answers["6"]["answer"])


# Submit new form using the data from above:
payload = {
    # Input Table
    "submission[3]": submission_answers["3"]["answer"],
    # Title
    "submission[4]": submission_answers["4"]["answer"],
    # Description
    "submission[5]": submission_answers["5"]["answer"],
    # Type
    "submission[6]": submission_answers["6"]["answer"],
}
print(payload)
url = f"https://api.jotform.com/form/{form_id}/submissions"
response = requests.request("POST", url, headers=headers, data=payload, files=files)
print(response)
