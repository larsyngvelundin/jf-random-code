import json
import os

from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.environ.get("JOTFORM_API_KEY")

id_list = {}
with open("fields.json", "r") as file:
    field_data = json.load(file)["content"]
    for id in field_data:
        if "text" in field_data[id]:
            id_list[field_data[id]["text"]] = id
print(id_list)


json_conditions = {}
with open("conditions.json", "r") as file:
    condition_data = json.load(file)["conditions"]
    for c_index, condition in enumerate(condition_data):
        json_conditions[f"properties[conditions][{c_index}][index]"] = c_index
        for k_index, (key, value) in enumerate(condition.items()):
            if key == "id" or key == "index" or key == "priority":
                pass
            elif key == "terms":
                terms = json.loads(condition[key])
                for t_index, term in enumerate(terms):
                    print(f"{term}")
                    for _, (t_key, t_value) in enumerate(term.items()):
                        if t_key == "id" or t_key == "isError":
                            pass
                        else:
                            print(
                                f"properties[conditions][{c_index}][terms][{t_index}][{t_key}]:{t_value}"
                            )
                            json_conditions[
                                f"properties[conditions][{c_index}][terms][{t_index}][{t_key}]"
                            ] = t_value
                pass
            elif key == "action":
                actions = json.loads(condition[key])
                for a_index, action in enumerate(actions):
                    print(f"{action}")
                    for _, (a_key, a_value) in enumerate(action.items()):
                        ignore = [
                            "id",
                            "isError",
                        ]
                        if a_key == "id" or a_key == "isError":
                            pass
                        else:
                            print(
                                f"properties[conditions][{c_index}][action][{a_index}][{a_key}]:{a_value}"
                            )
                            json_conditions[
                                f"properties[conditions][{c_index}][action][{a_index}][{a_key}]"
                            ] = a_value
                pass
            else:
                value = condition[key]
                json_conditions[f"properties[conditions][{c_index}][{key}]"] = value

c_index = 20
for index in range(2, 6):
    subtotal_a = id_list[f"{index} Subtotal A"]
    subtotal_b = id_list[f"{index} Subtotal B"]
    quantity_b = id_list[f"{index} Quantity B"]
    quantity_a = id_list[f"{index} Quantity A"]
    price_b = id_list[f"{index} Price B"]
    price_a = id_list[f"{index} Price A"]
    product_b = id_list[f"{index} Product B"]
    product_a = id_list[f"{index} Product A"]
    add_button = id_list[f"Add{index}"]
    json_conditions[f"properties[conditions][{c_index}][index]"] = c_index
    json_conditions[f"properties[conditions][{c_index}][action][0][replaceText]"] = ""
    json_conditions[f"properties[conditions][{c_index}][action][0][readOnly]"] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][newCalculationType]"
    ] = "True"
    json_conditions[f"properties[conditions][{c_index}][action][0][allowZeroCopy]"] = (
        "True"
    )
    json_conditions[
        f"properties[conditions][{c_index}][action][0][useCommasForDecimals]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][operands]"] = (
        f"{subtotal_b}"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][equation]"] = (
        f"{{{subtotal_b}}}"
    )
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showBeforeInput]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showEmptyDecimals]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][ignoreHiddenFields]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][insertAsText]"] = (
        "False"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][resultField]"] = (
        f"{subtotal_a}"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][decimalPlaces]"] = (
        "2"
    )
    json_conditions[f"properties[conditions][{c_index}][link]"] = "Any"
    json_conditions[f"properties[conditions][{c_index}][terms][0][field]"] = (
        f"{subtotal_b}"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][operator]"] = (
        "isFilled"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][value]"] = ""
    json_conditions[f"properties[conditions][{c_index}][type]"] = "calculation"
    c_index += 1
    # 2 ===============================
    json_conditions[f"properties[conditions][{c_index}][index]"] = c_index
    json_conditions[f"properties[conditions][{c_index}][action][0][replaceText]"] = ""
    json_conditions[f"properties[conditions][{c_index}][action][0][readOnly]"] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][newCalculationType]"
    ] = "True"
    json_conditions[f"properties[conditions][{c_index}][action][0][allowZeroCopy]"] = (
        "True"
    )
    json_conditions[
        f"properties[conditions][{c_index}][action][0][useCommasForDecimals]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][operands]"] = (
        f"{subtotal_a}"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][equation]"] = (
        f"{{{subtotal_a}}}"
    )
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showBeforeInput]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showEmptyDecimals]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][ignoreHiddenFields]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][insertAsText]"] = (
        "False"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][resultField]"] = (
        f"{subtotal_b}"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][decimalPlaces]"] = (
        "2"
    )
    json_conditions[f"properties[conditions][{c_index}][link]"] = "Any"
    json_conditions[f"properties[conditions][{c_index}][terms][0][field]"] = (
        f"{subtotal_a}"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][operator]"] = (
        "isFilled"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][value]"] = ""
    json_conditions[f"properties[conditions][{c_index}][type]"] = "calculation"
    c_index += 1
    # 3 ===============================
    json_conditions[f"properties[conditions][{c_index}][index]"] = c_index
    json_conditions[f"properties[conditions][{c_index}][action][0][replaceText]"] = ""
    json_conditions[f"properties[conditions][{c_index}][action][0][readOnly]"] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][newCalculationType]"
    ] = "True"
    json_conditions[f"properties[conditions][{c_index}][action][0][allowZeroCopy]"] = (
        "True"
    )
    json_conditions[
        f"properties[conditions][{c_index}][action][0][useCommasForDecimals]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][operands]"] = (
        f"{quantity_b}"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][equation]"] = (
        f"{{{quantity_b}}}"
    )
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showBeforeInput]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showEmptyDecimals]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][ignoreHiddenFields]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][insertAsText]"] = (
        "False"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][resultField]"] = (
        f"{quantity_a}"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][decimalPlaces]"] = (
        "2"
    )
    json_conditions[f"properties[conditions][{c_index}][link]"] = "Any"
    json_conditions[f"properties[conditions][{c_index}][terms][0][field]"] = (
        f"{quantity_b}"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][operator]"] = (
        "isFilled"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][value]"] = ""
    json_conditions[f"properties[conditions][{c_index}][type]"] = "calculation"
    c_index += 1
    # 4 ===============================
    json_conditions[f"properties[conditions][{c_index}][index]"] = c_index
    json_conditions[f"properties[conditions][{c_index}][action][0][replaceText]"] = ""
    json_conditions[f"properties[conditions][{c_index}][action][0][readOnly]"] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][newCalculationType]"
    ] = "True"
    json_conditions[f"properties[conditions][{c_index}][action][0][allowZeroCopy]"] = (
        "True"
    )
    json_conditions[
        f"properties[conditions][{c_index}][action][0][useCommasForDecimals]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][operands]"] = (
        f"{quantity_a}"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][equation]"] = (
        f"{{{quantity_a}}}"
    )
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showBeforeInput]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showEmptyDecimals]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][ignoreHiddenFields]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][insertAsText]"] = (
        "False"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][resultField]"] = (
        f"{quantity_b}"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][decimalPlaces]"] = (
        "2"
    )
    json_conditions[f"properties[conditions][{c_index}][link]"] = "Any"
    json_conditions[f"properties[conditions][{c_index}][terms][0][field]"] = (
        f"{quantity_a}"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][operator]"] = (
        "isFilled"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][value]"] = ""
    json_conditions[f"properties[conditions][{c_index}][type]"] = "calculation"
    c_index += 1
    # 5 ===============================
    json_conditions[f"properties[conditions][{c_index}][index]"] = c_index
    json_conditions[f"properties[conditions][{c_index}][action][0][replaceText]"] = ""
    json_conditions[f"properties[conditions][{c_index}][action][0][readOnly]"] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][newCalculationType]"
    ] = "True"
    json_conditions[f"properties[conditions][{c_index}][action][0][allowZeroCopy]"] = (
        "True"
    )
    json_conditions[
        f"properties[conditions][{c_index}][action][0][useCommasForDecimals]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][operands]"] = (
        f"{price_b}"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][equation]"] = (
        f"{{{price_b}}}"
    )
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showBeforeInput]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showEmptyDecimals]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][ignoreHiddenFields]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][insertAsText]"] = (
        "False"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][resultField]"] = (
        f"{price_a}"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][decimalPlaces]"] = (
        "2"
    )
    json_conditions[f"properties[conditions][{c_index}][link]"] = "Any"
    json_conditions[f"properties[conditions][{c_index}][terms][0][field]"] = (
        f"{price_b}"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][operator]"] = (
        "isFilled"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][value]"] = ""
    json_conditions[f"properties[conditions][{c_index}][type]"] = "calculation"
    c_index += 1
    # 6 ===============================
    json_conditions[f"properties[conditions][{c_index}][index]"] = c_index
    json_conditions[f"properties[conditions][{c_index}][action][0][replaceText]"] = ""
    json_conditions[f"properties[conditions][{c_index}][action][0][readOnly]"] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][newCalculationType]"
    ] = "True"
    json_conditions[f"properties[conditions][{c_index}][action][0][allowZeroCopy]"] = (
        "True"
    )
    json_conditions[
        f"properties[conditions][{c_index}][action][0][useCommasForDecimals]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][operands]"] = (
        f"{price_a}"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][equation]"] = (
        f"{{{price_a}}}"
    )
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showBeforeInput]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showEmptyDecimals]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][ignoreHiddenFields]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][insertAsText]"] = (
        "False"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][resultField]"] = (
        f"{price_b}"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][decimalPlaces]"] = (
        "2"
    )
    json_conditions[f"properties[conditions][{c_index}][link]"] = "Any"
    json_conditions[f"properties[conditions][{c_index}][terms][0][field]"] = (
        f"{price_a}"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][operator]"] = (
        "isFilled"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][value]"] = ""
    json_conditions[f"properties[conditions][{c_index}][type]"] = "calculation"
    c_index += 1
    # 7 ===============================
    json_conditions[f"properties[conditions][{c_index}][index]"] = c_index
    json_conditions[f"properties[conditions][{c_index}][action][0][replaceText]"] = ""
    json_conditions[f"properties[conditions][{c_index}][action][0][readOnly]"] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][newCalculationType]"
    ] = "True"
    json_conditions[f"properties[conditions][{c_index}][action][0][allowZeroCopy]"] = (
        "True"
    )
    json_conditions[
        f"properties[conditions][{c_index}][action][0][useCommasForDecimals]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][operands]"] = (
        f"{product_b}"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][equation]"] = (
        f"{{{product_b}}}"
    )
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showBeforeInput]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showEmptyDecimals]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][ignoreHiddenFields]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][insertAsText]"] = (
        "False"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][resultField]"] = (
        f"{product_a}"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][decimalPlaces]"] = (
        "2"
    )
    json_conditions[f"properties[conditions][{c_index}][link]"] = "Any"
    json_conditions[f"properties[conditions][{c_index}][terms][0][field]"] = (
        f"{product_b}"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][operator]"] = (
        "isFilled"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][value]"] = ""
    json_conditions[f"properties[conditions][{c_index}][type]"] = "calculation"
    c_index += 1
    # 8 ===============================
    json_conditions[f"properties[conditions][{c_index}][index]"] = c_index
    json_conditions[f"properties[conditions][{c_index}][action][0][replaceText]"] = ""
    json_conditions[f"properties[conditions][{c_index}][action][0][readOnly]"] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][newCalculationType]"
    ] = "True"
    json_conditions[f"properties[conditions][{c_index}][action][0][allowZeroCopy]"] = (
        "True"
    )
    json_conditions[
        f"properties[conditions][{c_index}][action][0][useCommasForDecimals]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][operands]"] = (
        f"{product_a}"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][equation]"] = (
        f"{{{product_a}}}"
    )
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showBeforeInput]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showEmptyDecimals]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][ignoreHiddenFields]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][insertAsText]"] = (
        "False"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][resultField]"] = (
        f"{product_b}"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][decimalPlaces]"] = (
        "2"
    )
    json_conditions[f"properties[conditions][{c_index}][link]"] = "Any"
    json_conditions[f"properties[conditions][{c_index}][terms][0][field]"] = (
        f"{product_a}"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][operator]"] = (
        "isFilled"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][value]"] = ""
    json_conditions[f"properties[conditions][{c_index}][type]"] = "calculation"
    c_index += 1
    # 9 ===============================
    json_conditions[f"properties[conditions][{c_index}][index]"] = c_index
    json_conditions[f"properties[conditions][{c_index}][action][0][replaceText]"] = ""
    json_conditions[f"properties[conditions][{c_index}][action][0][readOnly]"] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][newCalculationType]"
    ] = "True"
    json_conditions[f"properties[conditions][{c_index}][action][0][allowZeroCopy]"] = (
        "True"
    )
    json_conditions[
        f"properties[conditions][{c_index}][action][0][useCommasForDecimals]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][operands]"] = "11"
    json_conditions[f"properties[conditions][{c_index}][action][0][equation]"] = "{11}"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showBeforeInput]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showEmptyDecimals]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][ignoreHiddenFields]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][insertAsText]"] = (
        "False"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][resultField]"] = (
        f"{subtotal_a}"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][decimalPlaces]"] = (
        "2"
    )
    json_conditions[f"properties[conditions][{c_index}][link]"] = "All"
    json_conditions[f"properties[conditions][{c_index}][terms][0][field]"] = (
        f"{subtotal_b}"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][operator]"] = (
        "isEmpty"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][value]"] = ""
    json_conditions[f"properties[conditions][{c_index}][terms][1][field]"] = (
        f"{add_button}"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][1][operator]"] = (
        "isFilled"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][1][value]"] = ""
    json_conditions[f"properties[conditions][{c_index}][type]"] = "calculation"
    c_index += 1
    # 10 ===============================
    json_conditions[f"properties[conditions][{c_index}][index]"] = c_index
    json_conditions[f"properties[conditions][{c_index}][action][0][replaceText]"] = ""
    json_conditions[f"properties[conditions][{c_index}][action][0][readOnly]"] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][newCalculationType]"
    ] = "True"
    json_conditions[f"properties[conditions][{c_index}][action][0][allowZeroCopy]"] = (
        "True"
    )
    json_conditions[
        f"properties[conditions][{c_index}][action][0][useCommasForDecimals]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][operands]"] = "10"
    json_conditions[f"properties[conditions][{c_index}][action][0][equation]"] = "{10}"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showBeforeInput]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showEmptyDecimals]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][ignoreHiddenFields]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][insertAsText]"] = (
        "False"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][resultField]"] = (
        f"{quantity_a}"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][decimalPlaces]"] = (
        "2"
    )
    json_conditions[f"properties[conditions][{c_index}][link]"] = "All"
    json_conditions[f"properties[conditions][{c_index}][terms][0][field]"] = (
        f"{quantity_b}"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][operator]"] = (
        "isEmpty"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][value]"] = ""
    json_conditions[f"properties[conditions][{c_index}][terms][1][field]"] = (
        f"{add_button}"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][1][operator]"] = (
        "isFilled"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][1][value]"] = ""
    json_conditions[f"properties[conditions][{c_index}][type]"] = "calculation"
    c_index += 1
    # 11 ===============================
    json_conditions[f"properties[conditions][{c_index}][index]"] = c_index
    json_conditions[f"properties[conditions][{c_index}][action][0][replaceText]"] = ""
    json_conditions[f"properties[conditions][{c_index}][action][0][readOnly]"] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][newCalculationType]"
    ] = "True"
    json_conditions[f"properties[conditions][{c_index}][action][0][allowZeroCopy]"] = (
        "True"
    )
    json_conditions[
        f"properties[conditions][{c_index}][action][0][useCommasForDecimals]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][operands]"] = "7"
    json_conditions[f"properties[conditions][{c_index}][action][0][equation]"] = "{7}"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showBeforeInput]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showEmptyDecimals]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][ignoreHiddenFields]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][insertAsText]"] = (
        "False"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][resultField]"] = (
        f"{price_a}"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][decimalPlaces]"] = (
        "2"
    )
    json_conditions[f"properties[conditions][{c_index}][link]"] = "All"
    json_conditions[f"properties[conditions][{c_index}][terms][0][field]"] = (
        f"{price_b}"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][operator]"] = (
        "isEmpty"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][value]"] = ""
    json_conditions[f"properties[conditions][{c_index}][terms][1][field]"] = (
        f"{add_button}"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][1][operator]"] = (
        "isFilled"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][1][value]"] = ""
    json_conditions[f"properties[conditions][{c_index}][type]"] = "calculation"
    c_index += 1
    # 12 ===============================
    json_conditions[f"properties[conditions][{c_index}][index]"] = c_index
    json_conditions[f"properties[conditions][{c_index}][action][0][replaceText]"] = ""
    json_conditions[f"properties[conditions][{c_index}][action][0][readOnly]"] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][newCalculationType]"
    ] = "True"
    json_conditions[f"properties[conditions][{c_index}][action][0][allowZeroCopy]"] = (
        "True"
    )
    json_conditions[
        f"properties[conditions][{c_index}][action][0][useCommasForDecimals]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][operands]"] = "24"
    json_conditions[f"properties[conditions][{c_index}][action][0][equation]"] = "{24}"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showBeforeInput]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][showEmptyDecimals]"
    ] = "False"
    json_conditions[
        f"properties[conditions][{c_index}][action][0][ignoreHiddenFields]"
    ] = "False"
    json_conditions[f"properties[conditions][{c_index}][action][0][insertAsText]"] = (
        "False"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][resultField]"] = (
        f"{product_a}"
    )
    json_conditions[f"properties[conditions][{c_index}][action][0][decimalPlaces]"] = (
        "2"
    )
    json_conditions[f"properties[conditions][{c_index}][link]"] = "All"
    json_conditions[f"properties[conditions][{c_index}][terms][0][field]"] = (
        f"{product_b}"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][operator]"] = (
        "isEmpty"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][0][value]"] = ""
    json_conditions[f"properties[conditions][{c_index}][terms][1][field]"] = (
        f"{add_button}"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][1][operator]"] = (
        "isFilled"
    )
    json_conditions[f"properties[conditions][{c_index}][terms][1][value]"] = ""
    json_conditions[f"properties[conditions][{c_index}][type]"] = "calculation"
    c_index += 1


form_id = ""
url = f"https://api.jotform.com/form/{form_id}/properties"

payload = json_conditions

print("===============================")
print("===============================")
print("===============================")

last_index = ""
for thing in payload:
    if last_index != thing[21:25]:
        last_index = thing[21:25]
        print("===============================")
    print(f"{thing} : {payload[thing]}")

headers = {"apiKey": api_key}

response = requests.request("POST", url, headers=headers, data=payload)

print(response)
print(response.text)
response_json = json.loads(response.text)
print(response_json)
