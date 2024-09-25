count_orders = int(input())
current_coffee_price = 0
total_coffee_price = 0

for order in range(1, count_orders + 1):
    price_capsule = float(input())
    days = int(input())
    needed_capsules_daily = int(input())
    if not 0.01 <= price_capsule <= 100:
        continue
    elif not 1 <= days <= 31:
        continue
    elif not 1 <= needed_capsules_daily <= 2000:
        continue
    current_coffee_price = price_capsule * days * needed_capsules_daily
    print(f"The price for the coffee is: ${current_coffee_price:.2f}")
    total_coffee_price += current_coffee_price

print(f"Total: ${total_coffee_price:.2f}")
