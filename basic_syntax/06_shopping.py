budget = int(input())
total_spent = 0

while True:
    command = input()

    if command == "End":
        print("You bought everything needed.")
        break

    price = int(command)

    if price + total_spent <= budget:
        total_spent += price
    else:
        print("You went in overdraft!")
        break