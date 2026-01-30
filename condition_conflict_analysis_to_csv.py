import json
from conditions import conditions

print("================================")
print("================================")
print("================================")
active_conditions = []

for condition in conditions:
    if "disabled" in condition and condition["disabled"] == "1":
        continue
    if condition["type"] == "field":
        active_conditions.append(condition)

condition_types = {
    "HideMultiple": "hide",
    "Hide": "hide",
    "ShowMultiple": "show",
    "Show": "show",
}

result_fields = {}


def add_result_field(field, triggers, action):
    action = condition_types[action]
    if field not in result_fields:
        result_fields[field] = {}
    if action not in result_fields[field]:
        result_fields[field][action] = []
    for trigger in triggers:
        result_fields[field][action].append(trigger)


for condition in active_conditions:
    print("================================")
    print("================================")
    terms = json.loads(condition["terms"].replace("\\\xa0", " "))
    if len(terms) > 1:
        print(f"IF {condition['link']}:")
    else:
        print("IF:")
    triggers = []
    trigger_list_all = []
    for term in terms:
        operator = term["operator"]
        field_id = term["field"]
        value = term["value"]
        if condition["link"] == "All":
            trigger_list_all.append(f"{field_id} {operator} {value}")
        else:
            triggers.append([f"{field_id} {operator} {value}"])
        print(f" - IF field {field_id} is {operator} to {value}")
    if trigger_list_all:
        triggers.append(trigger_list_all)
    print("\nTHEN:")
    actions = json.loads(condition["action"])
    for action in actions:
        action_type = action["visibility"]
        if "fields" in action:
            for field in action["fields"]:
                print(f" - {condition_types[action_type]} {field}")
                add_result_field(field, triggers, action_type)
        else:
            field = action["field"]
            add_result_field(field, triggers, action_type)
            print(f" - {condition_types[action_type]} {field}")


for thing in result_fields:
    print("=====")
    print("=====")
    print(f"{thing}:\n{result_fields[thing]}")


print("===================")
print("===================")
print("CSV START")
print("===================")
print("===================")


print("unique rows (result fields)")
print("===================")
unique_rows = []
for field_id in result_fields:
    field = result_fields[field_id]
    for action in field:
        unique_rows.append(f"{field_id} {action}")
print(unique_rows)

print("===================")
print("unique columns (triggers)")
print("===================")
unique_columns = []
for field_id in result_fields:
    print("===================")
    print(f"== Field ID : {field_id} ==")
    print("===================")
    field = result_fields[field_id]
    print("===================")
    for action_type in field:
        action = field[action_type]
        print("     ===================")
        print(f"        {action_type} actions:")
        print("     ===================")
        print(f"        {action}")
        for term_set in action:
            column_name = "-".join(term_set)
            if column_name not in unique_columns:
                unique_columns.append(column_name)
            for term in term_set:
                print(f"            {term[:60]}")
print(unique_columns)
