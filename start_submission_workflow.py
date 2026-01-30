import os
import requests

from jotform import JotformAPIClient
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("JOTFORM_API_KEY")

submission_id = ""

start_workflow_url = (
    f"https://www.jotform.com/API/workflow/submission/{submission_id}/start"
)

headers = {
    "apiKey": api_key,
    "referer": "https://www.jotform.com/",
}

response = requests.post(start_workflow_url, headers=headers)
print("Status Code:", response.status_code)
if response.text.find("Cross-Site Requests") != -1:
    print("Response Content:", response.text)
elif response.status_code != 200:
    print(response.text)
else:
    print(f"Approval flow started for {submission_id}")
