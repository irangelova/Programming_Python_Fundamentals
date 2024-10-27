days_of_trip = int(input())
budget = float(input())
number_of_people = int(input())
fuel_price_per_km = float(input())
daily_food_expenses_per_person = float(input())
rooms_price_per_night_per_person = float(input())

total_price_food = daily_food_expenses_per_person * number_of_people * days_of_trip
total_price_accommodation = rooms_price_per_night_per_person * number_of_people * days_of_trip
if number_of_people > 10:
    total_price_accommodation -= 0.25 * total_price_accommodation
total_expenses = total_price_food + total_price_accommodation

expenses_daily_distance_travelled = 0
budget_exceeded = False

for day in range(1, days_of_trip + 1):
    distance_travelled = float(input())
    expenses_daily_distance_travelled = distance_travelled * fuel_price_per_km
    total_expenses += expenses_daily_distance_travelled

    if day % 3 == 0 or day % 5 == 0:
        total_expenses += 0.4 * total_expenses

    if day % 7 == 0:
        total_expenses -= total_expenses / number_of_people

    if total_expenses > budget:
        budget_exceeded = True
        break

if budget_exceeded:
    print(f"Not enough money to continue the trip. You need {(total_expenses - budget):.2f}$ more.")
else:
    print(f"You have reached the destination. You have {(budget - total_expenses):.2f}$ budget left.")

