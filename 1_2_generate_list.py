print("<ul>")
for i in range(1, 5):
    print(f'  <li class="order-{{number{i}}}">Number {i} : {{number{i}}}</li>')
print("</ul>")
