import requests
import os
import json
from time import sleep

api_key = ""
form_id = ""
# get all submission ids
url = f"https://api.jotform.com/form/{form_id}/submissions?apikey={api_key}&orderby=id&limit=1000&offset=0"

response = requests.get(url)
print("Status Code:", response.status_code)
if response.text.find("Cross-Site Requests") != -1:
    pass
elif response.status_code != 200:
    pass
else:
    data = json.loads(response.text)

submissions = data["content"]

pdf_ids = {
    "template 1": "",
    "template 2": "",
}
# loop through and download each pdf
for _, submission in enumerate(submissions):
    submission_id = submission["id"]
    try:
        first_name = submission["answers"]["3"]["answer"]["first"]
        last_name = submission["answers"]["3"]["answer"]["last"]
        print(f"{submission_id} - {last_name}, {first_name}")
        for pdf in pdf_ids:
            pdf_url = f"https://api.jotform.com/generatePDF?submissionid={submission_id}&apiKey={api_key}&reportid={pdf_ids[pdf]}&download=1&formid={form_id}"
            file_path = f"{pdf}/{last_name}, {first_name} - {pdf} - {submission_id}.pdf"
            response = requests.get(pdf_url)
            if response.status_code == 200:
                with open(file_path, "wb") as file:
                    file.write(response.content)
                print(f"File downloaded successfully ({submission_id})")
            else:
                print(
                    f"====================Failed to download {pdf} for {submission_id}"
                )
    except Exception as e:
        print(f"====================Failed {submission_id}: {e}")
