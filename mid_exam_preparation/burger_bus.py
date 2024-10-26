number_of_cities = int(input())
total_income = total_expenses = 0
total_profit = 0

for city in range(1, number_of_cities + 1):
    profit = 0
    name_of_the_city = input()
    owners_income = float(input())
    owners_expenses = float(input())

    if city % 3 == 0:
        owners_expenses += 0.5 * owners_expenses

    if city % 5 == 0:
        owners_income -= 0.1 * owners_income

    total_income += owners_income
    total_expenses += owners_expenses
    profit = owners_income - owners_expenses

    print(f"In {name_of_the_city} Burger Bus earned {profit:.2f} leva.")

total_profit += total_income - total_expenses
print(f"Burger Bus total profit: {total_profit:.2f} leva.")
