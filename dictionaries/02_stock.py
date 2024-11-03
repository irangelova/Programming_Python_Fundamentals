products = input().split()
product_stock = {}

for product in range(0, len(products), 2):
    key = products[product]
    value = products[product + 1]
    product_stock[key] = int(value)

products_to_search = input().split()

for searched_product in products_to_search:
    if searched_product in product_stock.keys():
        print(f"We have {product_stock[searched_product]} of {searched_product} left")
    else:
        print(f"Sorry, we don't have {searched_product}")
