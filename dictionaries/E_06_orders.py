products_quantity_dictionary = {}
products_price_dictionary = {}

while True:
    command = input()
    if command == "buy":
        break

    product = command.split()[0]
    price = float(command.split()[1])
    quantity = int(command.split()[2])

    if product not in products_quantity_dictionary.keys():
        products_quantity_dictionary[product] = 0
        products_price_dictionary[product] = 0
    products_price_dictionary[product] = price
    products_quantity_dictionary[product] += quantity

for product_, price_ in products_price_dictionary.items():
    total_price = price_ * products_quantity_dictionary[product_]
    print(f"{product_} -> {total_price:.2f}")

