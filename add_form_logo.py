import json
import requests

api_key = ""
form_id = ""
logo_url = ""

headers = {"apiKey": api_key}
url = f"https://api.jotform.com/form/{form_id}/properties"

# Get the current 'styleJSON'
response = requests.request("GET", url, headers=headers)
styleJSONstr = json.loads(response.text)["content"]["styleJSON"]
styleJSON = json.loads(styleJSONstr)

# Set a new Logo
styleJSON["@formCover"] = 1  # Enable, 0 = Disable
styleJSON["@formCoverImg"] = logo_url
# Optional parameters:
styleJSON["@formCoverImgWidth"] = 140
styleJSON["@formCoverImgHeight"] = 140
styleJSON["@formCoverPosition"] = "Top"
styleJSON["@formCoverTopPosition"] = "Center"
styleJSON["@formCoverBottomMargin"] = 32

# Convert the Dictionary back to a JSON string
newStyleJSONstr = json.dumps(styleJSON)

# POST the new styleJSON
payload = {"properties[styleJSON]": newStyleJSONstr}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
