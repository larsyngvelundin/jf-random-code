import os
from dotenv import load_dotenv
import requests
from time import sleep

load_dotenv()
api_key = os.environ.get("JOTFORM_API_KEY")
pdf_dir = "."


def download_pdf(form_id, item):
    sleep(5)
    try:
        os.mkdir(os.path.join(pdf_dir, item))
    except Exception:
        pass
    pdf_path = os.path.join(pdf_dir, item, item + ".pdf")

    base_url = "https://jotform.com/server.php"
    params = {
        "action": "getSubmissionPDF",
        "sid": item,
        "formID": form_id,
        "apiKey": api_key,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        with open(pdf_path, "wb") as f:
            f.write(response.content)
        print(f"Success: {pdf_path}")
    else:
        print("Failed:", response.status_code)


submission_id = ""
form_id = ""
download_pdf(form_id=form_id, item=submission_id)
