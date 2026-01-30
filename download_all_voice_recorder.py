import json
import requests

api_key = ""
submission_id = ""

headers = {"apiKey": api_key}
url = f"https://api.jotform.com/submission/{submission_id}"

response = requests.request("GET", url, headers=headers)
text = json.loads(response.text)
fields = text["content"]["answers"]


def download_file(url, local_filename):
    with requests.get(url, stream=True, headers=headers) as r:
        print(r)
        r.raise_for_status()
        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        return local_filename


for id in fields:
    if "cfname" in fields[id]:
        if fields[id]["cfname"] == "Voice Recorder":
            file_name = fields[id]["text"][:20]  # first 20 characters
            download_link = fields[id]["answer"]
            download_file(f"https://www.jotform.com{download_link}", f"{file_name}.wav")
