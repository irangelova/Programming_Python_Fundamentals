def important_products(products: list, product: str) -> list:
    if product in products:
        products.pop(products.index(product))
        products.insert(0, product)
    else:
        products.insert(0, product)
    return products


def add_product(products: list, product: str) -> list and bool:
    if product not in products:
        products.append(product)
        return products, False
    else:
        products = products
        return products, True


def swap_products(products: list, product1: str, product2: str):
    if product1 in products and product2 in products:
        first_index = int(products.index(product1))
        second_index = int(products.index(product2))
        products[first_index], products[second_index] = products[second_index], products[first_index]
        return products, False, product1
    elif product1 not in products:
        return products, True, product1
    elif product2 not in products:
        return products, True, product2


def remove_product(products: list, product: str):
    if product in products:
        products.pop(products.index(product))
        return products, False, product
    else:
        return products, True, product


products_list = input().split("|")
product_already_in_list = False
is_product_missing = False
product_missing = ""

while True:
    command = input()

    if command == "Shop!":
        break

    if command == "Reversed":
        products_list.reverse()

    action = command.split("%")[0]
    if action == "Important":
        important_product = command.split("%")[1]
        products_list = important_products(products_list, important_product)
    elif action == "Add":
        product_to_add = command.split("%")[1]
        products_list, product_already_in_list = add_product(products_list, product_to_add)
        if product_already_in_list:
            print("The product is already in the list.")
    elif action == "Swap":
        first_product = command.split("%")[1]
        second_product = command.split("%")[2]
        products_list, is_product_missing, product_missing = swap_products(products_list, first_product, second_product)
        if is_product_missing:
            print(f"Product {product_missing} missing!")
    elif action == "Remove":
        product_to_remove = command.split("%")[1]
        products_list, is_product_missing, product_missing = remove_product(products_list, product_to_remove)
        if is_product_missing:
            print(f"Product {product_missing} isn't in the list.")

for position in range(1, len(products_list) + 1):
    print(f"{position}. {products_list[position - 1]}")
