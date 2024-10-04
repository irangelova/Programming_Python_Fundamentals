item_prices = input().split("|")
budget = float(input())
ticket_price = 150
money_spent = money_received = 0
items_bought = []
items_sold = []

for item in range(len(item_prices)):
    current_item = (item_prices[item]).split("->")
    item_name = current_item[0]
    item_price = float(current_item[1])

    if item_name == "Clothes":
        if item_price <= 50:
            if budget >= item_price:
                budget -= item_price
                money_spent += item_price
                items_bought.append(item_price)
                new_price = item_price * 1.4
                money_received += new_price
                items_sold.append(f"{new_price:.2f}")
    elif item_name == "Shoes":
        if item_price <= 35:
            if budget >= item_price:
                budget -= item_price
                money_spent += item_price
                items_bought.append(item_price)
                new_price = item_price * 1.4
                money_received += new_price
                items_sold.append(f"{new_price:.2f}")
    elif item_name == "Accessories":
        if item_price <= 20.50:
            if budget >= item_price:
                budget -= item_price
                money_spent += item_price
                items_bought.append(item_price)
                new_price = item_price * 1.4
                money_received += new_price
                items_sold.append(f"{new_price:.2f}")

print(" ".join(items_sold))
profit = money_received - money_spent
print(f"Profit: {profit:.2f}")
budget += money_received
if budget >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")
