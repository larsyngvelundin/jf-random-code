from dotenv import load_dotenv
import requests, json, os
from time import sleep

load_dotenv()

api_key = os.environ.get("JOTFORM_API_KEY")
form_id = os.environ.get("JOTFORM_FORM_ID")
headers = {"apiKey": api_key}
offset = 0
limit = 3
all_submissions = []
while True:
    submissions_url = f"https://api.jotform.com/form/{form_id}/submissions?limit={limit}&offset={offset}"
    response = requests.request("GET", submissions_url, headers=headers)
    submissions = json.loads(response.text)["content"]
    all_submissions.extend(submissions)
    offset += limit
    print(f"Saved {len(all_submissions)} submissions so far.")
    sleep(1)
    if len(submissions) < limit:
        break
print(f"Complete, 'all_submissions' now contain {len(all_submissions)} submissions")
