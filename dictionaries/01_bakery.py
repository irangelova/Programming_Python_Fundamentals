products = input().split()
bakery_products = {}

for product in range(0, len(products), 2):
    key = products[product]
    value = products[product + 1]
    bakery_products[key] = int(value)

print(bakery_products)
