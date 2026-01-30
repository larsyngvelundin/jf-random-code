import requests

api_key = ""
submission_id = ""
form_id = ""
url = f"https://www.jotform.com/server.php?sheets=1&id={submission_id}&formID={form_id}&action=completePending&apiKey={api_key}"
headers = {"apiKey": api_key, "referer": f"https://www.jotform.com/tables/{form_id}"}
response = requests.post(url, headers=headers)
print("Response Content:", response.text)

print("Status Code:", response.status_code)
if response.text.find("Cross-Site Requests") != -1:
    print("Response Content:", response.text)
else:
    print(f"Submission marked as complete {submission_id}")

    print("Response Content:", response.text)
