sum_parts_before_tax = 0

while True:
    command = input()

    if command == "special" or command == "regular":
        break

    parts_price = float(command)
    if parts_price < 0:
        print("Invalid price!")
    else:
        sum_parts_before_tax += parts_price

sum_parts_after_tax = sum_parts_before_tax * 1.2
if command == "special":
    total_sum = 0.9 * sum_parts_after_tax
else:
    total_sum = sum_parts_after_tax

if total_sum == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {sum_parts_before_tax:.2f}$")
    print(f"Taxes: {(sum_parts_after_tax - sum_parts_before_tax):.2f}$")
    print("-----------")
    print(f"Total price: {total_sum:.2f}$")



