print("ul.sorted-results{display:grid}")
print("div.ty-bar-fill{background-color:orange}")

for i in range(0, 101):
    print(f"li.value-{i}{{order:{100 - i};}}")
    print(f"div.ty-bar-fill.value-{i}{{width:{i}%;}}")
