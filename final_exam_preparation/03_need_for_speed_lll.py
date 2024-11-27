number_of_cars = int(input())
car_park = {}

for _ in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    car_park[car] = {"mileage": int(mileage), "fuel": int(fuel)}

while True:
    command = input().split(" : ")
    if command[0] == "Stop":
        break
    elif command[0] == "Drive":
        current_car = command[1]
        current_distance = int(command[2])
        current_fuel = int(command[3])
        if car_park[current_car]["fuel"] < current_fuel:
            print("Not enough fuel to make that ride")
        else:
            car_park[current_car]["fuel"] -= current_fuel
            car_park[current_car]["mileage"] += current_distance
            print(f"{current_car} driven for {current_distance} kilometers. {current_fuel} liters of fuel consumed.")
            if car_park[current_car]["mileage"] >= 100000:
                car_park.pop(current_car)
                print(f"Time to sell the {current_car}!")
    elif command[0] == "Refuel":
        current_car = command[1]
        current_fuel = int(command[2])
        if (current_fuel + car_park[current_car]["fuel"]) > 75:
            added_fuel = 75 - car_park[current_car]["fuel"]
            car_park[current_car]["fuel"] = 75
        else:
            car_park[current_car]["fuel"] += current_fuel
            added_fuel = current_fuel
        print(f"{current_car} refueled with {added_fuel} liters")
    elif command[0] == "Revert":
        current_car = command[1]
        current_kilometer = int(command[2])
        if (car_park[current_car]["mileage"] - current_kilometer) > 10000:
            car_park[current_car]["mileage"] -= current_kilometer
            print(f"{current_car} mileage decreased by {current_kilometer} kilometers")
        else:
            car_park[current_car]["mileage"] = 10000

for car_, data in car_park.items():
    print(f"{car_} -> Mileage: {data['mileage']} kms, Fuel in the tank: {data['fuel']} lt.")
