def order_calculator(product, quantity):
    if product == "coffee":
        price = 1.5 * quantity
        return price
    elif product == "coke":
        price = 1.4 * quantity
        return price
    elif product == "water":
        price = 1.0 * quantity
        return price
    elif product == "snacks":
        price = 2.0 * quantity
        return price


chosen_product = input()
chosen_quantity = int(input())
total_price = order_calculator(chosen_product, chosen_quantity)
print(f"{total_price:.2f}")