from jotform import JotformAPIClient
import requests
import base64
import json
import dotenv
import os

dotenv.load_dotenv()
api_key = os.environ.get("JOTFORM_API")
print(api_key[:5])

form_id = ""

# jotformAPI = JotformAPIClient(api_key)

# submission = {"3_name": "Test", "4_email": "test@gmail.com"}
# response = jotformAPI.create_form_submission(form_id, submission)
# submission_id = response["submissionID"]

# # Direct to submission
# print(f"https://jotform.com/submission/{submission_id}")
# # Direct to submission in Inbox
# print(f"https://jotform.com/inbox/{form_id}/{submission_id}")

# exit()

# submission_id = ""

form_questions_url = f"https://api.jotform.com/form/{form_id}/questions"

headers = {
    "apiKey": api_key,
    "referer": "https://www.jotform.com/",
}

response = requests.get(form_questions_url, headers=headers)
print("Status Code:", response.status_code)
if response.text.find("Cross-Site Requests") != -1:
    print("Response Content:", response.text)
elif response.status_code != 200:
    print(response.text)
else:
    # print(f"Approval flow started for {submission_id}")
    questions = json.loads(response.text)["content"]
    for id in questions:
        q = questions[id]
        if q["type"] == "control_fileupload":
            print(f"{q['qid']}_{q['name']}")

# question 3
# 3_fileUpload

field_name = "3_fileUpload"
# file_name = "Podo-Avatar2-02.png"
# qqfile = "Podo-Avatar2-02.png"
file_name = "podo_2.png"
# qqfile = "testfile.txt"
upload_url = (
    "https://upload.jotform.com/upload"
    + "?action=multipleUpload"
    + f"&field={field_name}"
    + f"&folder={form_id}"
    + f"&name={file_name}"
    + f"&qqfile={file_name}"
)

# with open(file_name, "rb") as file:
# file_content = base64.b64encode(file.read())
with open(file_name, "rb") as file:
    file_content = file.read()
# with open(file_name, "r", encoding="utf-8") as file:
#     file_content = file.read()
print("#" * 20)
print(file_content[:300])
print(file_content[-300:])
print("#" * 20)

payload = file_content
response = requests.post(upload_url, headers=headers, data=payload)
if response.text.find("Cross-Site Requests") != -1:
    print("Response Content:", response.text)
elif response.status_code != 200:
    print(response.text)
else:
    print(response.text)
    file_info = json.loads(response.text)
    # questions = json.loads(response.text)["content"]
    # for id in questions:
    #     print(questions[id])


submit_url = f"https://api.jotform.com/form/{form_id}/submissions"
file_server = file_info["fileServer"]
file_message = file_info["message"]
payload = {
    "submission[3]": f"{file_message}",
    "temp_upload[q3_fileUpload][]": f"{file_message}#{file_server}",
    "file_server": f"{file_server}",
}

response = requests.post(submit_url, headers=headers, data=payload)
print("Status Code:", response.status_code)
if response.text.find("Cross-Site Requests") != -1:
    print("Response Content:", response.text)
elif response.status_code != 200:
    print(response.text)
else:
    print(response.text)
    # print(f"Approval flow started for {submission_id}")
    # questions = json.loads(response.text)["content"]
    # for id in questions:
    #     print(questions[id])
