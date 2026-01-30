import requests, json, os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("JOTFORM_API_KEY")
form_id = os.environ.get("JOTFORM_FORM_ID")

headers = {"apiKey": api_key}

# Get the reports for the form
form_reports_url = f"https://api.jotform.com/form/{form_id}/reports"
response = requests.request("GET", form_reports_url, headers=headers)
reports = json.loads(response.text)["content"]

for report in reports:
    # Checking if report is still enabled, i.e. not trashed or disabled
    if report["status"] == "ENABLED":
        # Get the report URL
        report_url = report["url"]
        # Download the report using the URL
        with requests.get(report_url, stream=True, headers=headers) as result:
            result.raise_for_status()
            file_name = f"{report['title']}.xlsx"
            # Save the file from the request result
            with open(file_name, "wb") as file:
                for chunk in result.iter_content(chunk_size=8192):
                    file.write(chunk)
        print(
            f"Report '{report['title']}' ({report['id']}) was downloaded and saved as '{file_name}'"
        )
    else:
        print(
            f"Report '{report['title']}' ({report['id']}) was not downloaded as its status is '{report['status']}'"
        )
