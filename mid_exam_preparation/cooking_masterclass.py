from math import ceil

budget = float(input())
students = int(input())
price_per_package_flour = float(input())
price_per_egg = float(input())
price_per_apron = float(input())

total_price_flour = students * price_per_package_flour
if students % 5 == 0:
    free_packages = students // 5
    total_price_flour -= free_packages * price_per_package_flour
total_price_eggs = students * 10 * price_per_egg
total_price_apron = (students + ceil(students * 0.2)) * price_per_apron

total_price_items = total_price_flour + total_price_eggs + total_price_apron

if budget >= total_price_items:
    print(f"Items purchased for {total_price_items:.2f}$.")
else:
    print(f"{(total_price_items - budget):.2f}$ more needed.")