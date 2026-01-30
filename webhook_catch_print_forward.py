from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
FORWARD_URL = ""


@app.route("/webhook", methods=["POST", "GET"])
def webhook():
    if request.method == "POST":
        print(1)
        print(request)
        print(dir(request))
        print(request.form)
        print(request.headers)
        custom_header = {
            "Content-Type": "multipart/form-data; boundary=------------------------DqYzhvlvQjJIvUKSfr9fyZ"
        }
        response = requests.post(FORWARD_URL, headers=custom_header, json="{}")
        print(2)
        print("Status Code:", response.status_code)
        print(3)
        print("Response Body:", response.content)
        print(4)
        return jsonify({"status": "success", "data": response.json()}), 200
        print(5)
    else:
        return "Not POST", 200


if __name__ == "__main__":
    app.run(port=5000)
