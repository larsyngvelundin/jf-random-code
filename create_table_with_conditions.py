import csv
import requests
import json
import sys
from time import sleep

apiKey = ""
form_id = ""
field_url = f"https://api.jotform.com/form/{form_id}/questions"

headers = {"apiKey": apiKey}

# Reading the CSV file
print("Reading the CSV file")
if len(sys.argv) != 2:
    print("Usage: python script.py path/to/file.csv")
    sys.exit(1)

product_names, product_weights = [], []
file_path = sys.argv[1]
with open(file_path, mode="r", newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        product_names.append(row[0])
        product_weights.append(row[1])

product_names.pop(0)
product_weights.pop(0)


# Creating the Input Table
print("Creating the Input Table")
table_payload = {
    "question[type]": "control_matrix",
    "question[mcolumns]": "Quantity",
    "question[mrows]": "|".join(product_names),
    "question[order]": "2",
    "question[inputType]": "Numeric Text Box",
    "question[text]": "Haki Components",
    "question[matrixcells]": "150",
    "question[matrixwidth]": "650",
}
response = requests.request(
    "POST", field_url, headers=headers, data=table_payload, files=[]
)
response_json = json.loads(response.text)
input_table_id = response_json["content"]["qid"]


# Creating Total Quantity
print("Creating Total Quantity")
quantity_payload = {
    "question[type]": "control_calculation",
    "question[defaultResult]": "0",
    "question[order]": 3,
    "question[required]": "No",
    "question[text]": f"Total Quantity",
    "question[widgetType]": "native",
}
response = requests.request(
    "POST", field_url, headers=headers, data=quantity_payload, files=[]
)
response_json = json.loads(response.text)
quantity_id = response_json["content"]["qid"]


# Creating Total Weight
print("Creating Total Weight")
weight_payload = {
    "question[type]": "control_calculation",
    "question[defaultResult]": "0",
    "question[order]": 3,
    "question[required]": "No",
    "question[text]": f"Total Weight",
    "question[widgetType]": "native",
}
response = requests.request(
    "POST", field_url, headers=headers, data=weight_payload, files=[]
)
response_json = json.loads(response.text)
weight_id = response_json["content"]["qid"]

print("Creating Calc Widgets")
calc_widget_ids = []
for i in range(0, len(product_names)):
    print(f"{i + 1}/{len(product_names)} calculation widgetscreated")
    trying = True
    while trying:
        try:
            calc_widget_payload = {
                "question[type]": "control_calculation",
                "question[defaultResult]": "0",
                "question[order]": str(5 + i),
                "question[required]": "No",
                "question[hidden]": "Yes",
                "question[text]": f"{product_names[i]} - W",
                "question[widgetType]": "native",
            }
            response = requests.request(
                "POST", field_url, headers=headers, data=calc_widget_payload, files=[]
            )
            response_json = json.loads(response.text)
            calc_widget_ids.append(response_json["content"]["qid"])
            trying = False
        except Exception:
            print("Probably API rate limit, waiting 10 seconds.")
            sleep(10)


calculation_url = f"https://api.jotform.com/form/{form_id}/properties"
print("Creating calculations")
calculation_payload = {}


# Adding Quantity
calculation_payload[
    f"properties[calculations][{len(product_names) + 1}][allowZeroCopy]"
] = "1"
calculation_payload[
    f"properties[calculations][{len(product_names) + 1}][decimalPlaces]"
] = "2"
equation = "["
for i in range(0, len(product_weights)):
    equation += f"{{{input_table_id}_{i}_0}}+"
equation = equation[:-1]
equation += "]"
# print(f"equation: {equation}")
calculation_payload[f"properties[calculations][{len(product_names) + 1}][equation]"] = (
    equation
)
calculation_payload[
    f"properties[calculations][{len(product_names) + 1}][ignoreHiddenFields]"
] = "0"
calculation_payload[
    f"properties[calculations][{len(product_names) + 1}][insertAsText]"
] = "0"
calculation_payload[
    f"properties[calculations][{len(product_names) + 1}][newCalculationType]"
] = "1"
calculation_payload[f"properties[calculations][{len(product_names) + 1}][operands]"] = (
    input_table_id
)
calculation_payload[f"properties[calculations][{len(product_names) + 1}][readOnly]"] = (
    "0"
)
calculation_payload[
    f"properties[calculations][{len(product_names) + 1}][replaceText]"
] = ""
calculation_payload[
    f"properties[calculations][{len(product_names) + 1}][resultField]"
] = quantity_id
calculation_payload[
    f"properties[calculations][{len(product_names) + 1}][showEmptyDecimals]"
] = "0"
calculation_payload[
    f"properties[calculations][{len(product_names) + 1}][showBeforeInput]"
] = "0"
calculation_payload[
    f"properties[calculations][{len(product_names) + 1}][useCommasForDecimals]"
] = "0"

# Adding Weight
calculation_payload[
    f"properties[calculations][{len(product_names) + 2}][allowZeroCopy]"
] = "1"
calculation_payload[
    f"properties[calculations][{len(product_names) + 2}][decimalPlaces]"
] = "2"
equation = "["
for i in range(0, len(product_weights)):
    equation += f"{{{calc_widget_ids[i]}}}+"
equation = equation[:-1]
equation += "]"
calculation_payload[f"properties[calculations][{len(product_names) + 2}][equation]"] = (
    equation
)
calculation_payload[
    f"properties[calculations][{len(product_names) + 2}][ignoreHiddenFields]"
] = "0"
calculation_payload[
    f"properties[calculations][{len(product_names) + 2}][insertAsText]"
] = "0"
calculation_payload[
    f"properties[calculations][{len(product_names) + 2}][newCalculationType]"
] = "1"
calculation_payload[f"properties[calculations][{len(product_names) + 2}][operands]"] = (
    calc_widget_ids[0]
)
calculation_payload[f"properties[calculations][{len(product_names) + 2}][readOnly]"] = (
    "0"
)
calculation_payload[
    f"properties[calculations][{len(product_names) + 2}][replaceText]"
] = ""
calculation_payload[
    f"properties[calculations][{len(product_names) + 2}][resultField]"
] = weight_id
calculation_payload[
    f"properties[calculations][{len(product_names) + 2}][showEmptyDecimals]"
] = "0"
calculation_payload[
    f"properties[calculations][{len(product_names) + 2}][showBeforeInput]"
] = "0"
calculation_payload[
    f"properties[calculations][{len(product_names) + 2}][useCommasForDecimals]"
] = "0"


for i in range(0, len(product_names)):
    calculation_payload[f"properties[calculations][{i}][allowZeroCopy]"] = "1"
    calculation_payload[f"properties[calculations][{i}][decimalPlaces]"] = "2"
    equation = f"[{{{input_table_id}_{i}_0}}*{product_weights[i]}]"
    calculation_payload[f"properties[calculations][{i}][equation]"] = equation
    calculation_payload[f"properties[calculations][{i}][ignoreHiddenFields]"] = "0"
    calculation_payload[f"properties[calculations][{i}][insertAsText]"] = "0"
    calculation_payload[f"properties[calculations][{i}][newCalculationType]"] = "1"
    calculation_payload[f"properties[calculations][{i}][operands]"] = input_table_id
    calculation_payload[f"properties[calculations][{i}][readOnly]"] = "0"
    calculation_payload[f"properties[calculations][{i}][replaceText]"] = ""
    calculation_payload[f"properties[calculations][{i}][resultField]"] = (
        calc_widget_ids[i]
    )
    calculation_payload[f"properties[calculations][{i}][showEmptyDecimals]"] = "0"
    calculation_payload[f"properties[calculations][{i}][showBeforeInput]"] = "0"
    calculation_payload[f"properties[calculations][{i}][useCommasForDecimals]"] = "0"

response = requests.request(
    "POST", calculation_url, headers=headers, data=calculation_payload, files=[]
)
response_json = json.loads(response.text)
print(response_json["responseCode"])
