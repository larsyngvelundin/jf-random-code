print("""#cid_7 tr.form-matrix-value-tr{
    display: none;
}
""")
selector = ""
for i in range(0, 45):
    selector += f".form-all:has(#input_8_{i}:checked) #cid_7 tr.form-matrix-value-tr:nth-child({i + 2}),"
print(selector[:-1] + "{")
print("    display: table-row;")
print("}")
