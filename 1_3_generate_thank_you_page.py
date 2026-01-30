value_list = [
    "{judgeValue}",
    "{controllerValue}",
    "{sticklerValue}",
    "{pleaserValue}",
    "{restlessValue}",
    "{hyperachiever50}",
    "{victimValue}",
    "{hyperrationalValue}",
    "{hypervigilantValue}",
    "{avoiderValue}",
]

title_list = [
    "Judge:",
    "Controller:",
    "Stickler:",
    "Pleaser:",
    "Restless:",
    "Hyper-Achiever:",
    "Victim:",
    "Hyper-Rational:",
    "Hyper-Vigilant:",
    "Avoider:",
]

print('<ul class="sorted-results">')

for i in range(0, 10):
    print(f'<li class="value-{value_list[i]}"> ')
    print(f"""
<div class="ty-bar-title">{title_list[i]}</div>
    <div class="ty-bar-container">
        <div class="ty-bar-fill value-{value_list[i]}">{value_list[i]}</div>
    </div>
</div>""")
    print(f"</li>")


print("</ul>")
