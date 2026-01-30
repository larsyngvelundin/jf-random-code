import os, json
from dotenv import load_dotenv
import requests
from time import sleep

load_dotenv()
api_key = os.environ.get("JF_API_KEY")
if not api_key:
    print("No API Key set in .env, quitting")
    quit()

form_id = ""
headers = {
    "apiKey": api_key,
}
url_base = f"https://api.jotform.com/form/{form_id}/submissions"

offset = 0
all_submissions = []

while True:
    print(f"Fetching {offset}-{offset + 999}")
    url = url_base + f"?limit=1000&offset={offset}"
    response = requests.get(url, headers=headers)
    result = json.loads(response.text)
    print(result["resultSet"])
    if not result["resultSet"]["count"]:
        break
    offset += 1000
    for submission in result["content"]:
        all_submissions.append(submission)
    sleep(5)

print(f"Fetched all submissions ({len(all_submissions)})")


print("Checking submissions for duplicates")
duplicates = {}
seen = {}
for index, submission in enumerate(all_submissions):
    key = (
        submission["answers"]["29"]["answer"],
        submission["answers"]["30"]["answer"],
        submission["answers"]["26"]["answer"],
        submission["answers"]["19"]["answer"],
        submission["answers"]["25"]["answer"],
    )
    if key in seen:
        if key not in duplicates:
            duplicates[key] = [seen[key]]
        duplicates[key].append(submission["id"])
    else:
        seen[key] = submission["id"]
    break


for key, indices in duplicates.items():
    print(f"Duplicate answers {key} found at indices: {indices}")
if not duplicates:
    print("Found 0 duplicates")
