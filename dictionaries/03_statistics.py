bakery_products = {}

while True:
    command = input()

    if command == "statistics":
        break

    key = command.split(": ")[0]
    value = int(command.split(": ")[1])

    if key not in bakery_products.keys():
        bakery_products[key] = value
    else:
        bakery_products[key] += value

print("Products in stock:")
for key, value in bakery_products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(bakery_products.keys())}")
print(f"Total Quantity: {sum(bakery_products.values())}")

