import time
import json
import requests
import webhook_listener
import urllib3

http = urllib3.PoolManager()

api_key = ""
form_id = ""
question_id = ""


def process_post_request(request, *args, **kwargs):
    request_answers = json.loads(kwargs["rawRequest"])
    other_answer = request_answers["q5_ifNot"]
    url = f"https://api.jotform.com/form/{form_id}/question/{question_id}?apikey={api_key}"
    response = requests.get(url)
    response_dict = json.loads(response.text)
    all_options = response_dict["content"]["list"]
    if all_options.find(other_answer) != -1:
        print("Option already present")
    else:
        print("Option not present, adding")
        payload = {"question[list]": all_options + "\n" + other_answer}
        response = requests.request("POST", url, headers={}, data=payload, files=[])
        print(response.text)
    return


webhooks = webhook_listener.Listener(handlers={"POST": process_post_request})
webhooks.start()

while True:
    print("Still alive...")
    time.sleep(300)
