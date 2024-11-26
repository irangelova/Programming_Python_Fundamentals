stock_dictionary = {}
total_sold_quantity = 0

while True:
    command = input().split()

    if command[0] == "Complete":
        break
    elif command[0] == "Receive":
        quantity = int(command[1])
        food = command[2]
        if quantity <= 0:
            stock_dictionary = stock_dictionary
        elif food not in stock_dictionary.keys():
            stock_dictionary[food] = 0
        stock_dictionary[food] += quantity
    elif command[0] == "Sell":
        quantity = int(command[1])
        food = command[2]
        if food not in stock_dictionary.keys():
            print(f"You do not have any {food}.")
        elif stock_dictionary[food] < quantity:
            sold_quantity = stock_dictionary.pop(food)
            print(f"There aren't enough {food}. You sold the last {sold_quantity} of them.")
            total_sold_quantity += sold_quantity
        else:
            stock_dictionary[food] -= quantity
            print(f"You sold {quantity} {food}.")
            total_sold_quantity += quantity
            if stock_dictionary[food] == 0:
                stock_dictionary.pop(food)

for food, quantity in stock_dictionary.items():
    print(f"{food}: {quantity}")
print(f"All sold: {total_sold_quantity} goods")

