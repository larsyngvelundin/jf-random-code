for i in range(1, 11):
    print(f"""
.form-product-item:has(#input_28_1124):has(option[value="{i}"]:checked):after{{
    content: "({i * 25} tickets)" !important;
}}""")
