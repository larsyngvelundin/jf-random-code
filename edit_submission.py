import requests

api_key = ""
submission_id = ""

update_data = {
    "submission[4][first]": "Joe",
    "submission[4][last]": "Smith",
    "submission[new]": "1",
}

# POST request with form data
response = requests.post(
    f"https://api.jotform.com/submission/{submission_id}?apiKey={api_key}",
    data=update_data,
)

if response.status_code == 200:
    print("Submission updated successfully!")

else:
    print(f"Error updating submission: {response.text}")
