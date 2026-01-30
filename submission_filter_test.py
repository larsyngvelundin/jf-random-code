import os, json
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.environ.get("JOTFORM_API_KEY")
if not api_key:
    print("No API Key set in .env, quitting")
    quit()

form_id = ""
headers = {
    "apiKey": api_key,
}
url_base = f'https://api.jotform.com/form/{form_id}/submissions?&filter={{"'

for i in range(0, 30):
    url = url_base + f'created_at:gt":"2025-03-11 02:{str(i)}:00' + '"}'
    response = requests.get(url, headers=headers)
    print(response.text)
