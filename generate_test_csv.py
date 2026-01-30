row_count = input("How many rows?")
csv_content = "Unique ID,Text\n"
for i in range(1, int(row_count) + 1):
    csv_content += f"{i},Prefill for row {i}\n"
with open("file.csv", "w") as file:
    file.write(csv_content)
