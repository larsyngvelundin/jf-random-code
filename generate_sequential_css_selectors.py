for i in range(1, 31):
    print(
        f".form-section:has(#id_3 .form-checkbox-item:nth-child({i}) input:checked) #id_37 .form-checkbox-item:nth-child({i})",
        end="",
    )
    if i < 30:
        print(",")
