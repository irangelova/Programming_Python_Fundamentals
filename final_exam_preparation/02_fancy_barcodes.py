import re

count_of_barcodes = int(input())
pattern1 = r"(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])\1"
pattern2 = r"\d+"

for code in range(count_of_barcodes):
    barcode = input()
    search_barcode = re.search(pattern1, barcode)
    group_matches = re.findall(pattern2, barcode)
    print(group_matches)
    if group_matches:
        product_group = "".join(group_matches)
    else:
        product_group = "00"
    if search_barcode:
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
