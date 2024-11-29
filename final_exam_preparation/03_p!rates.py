cities_data = {}

while True:
    command1 = input().split("||")
    if command1[0] == "Sail":
        break
    city, population, gold = command1[0], int(command1[1]), int(command1[2])
    if city in cities_data.keys():
        cities_data[city]["population"] += population
        cities_data[city]["gold"] += gold
    else:
        cities_data[city] = {"population": population, "gold": gold}

while True:
    command2 = input().split("=>")
    if command2[0] == "End":
        break
    elif command2[0] == "Plunder":
        town = command2[1]
        people = int(command2[2])
        current_gold = int(command2[3])
        cities_data[town]["population"] -= people
        cities_data[town]["gold"] -= current_gold
        print(f"{town} plundered! {current_gold} gold stolen, {people} citizens killed.")
        if cities_data[town]["population"] == 0 or cities_data[town]["gold"] == 0:
            cities_data.pop(town)
            print(f"{town} has been wiped off the map!")
    elif command2[0] == "Prosper":
        town = command2[1]
        current_gold = int(command2[2])
        if current_gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities_data[town]["gold"] += current_gold
            print(f"{current_gold} gold added to the city treasury. {town} now has {cities_data[town]['gold']} gold.")

if cities_data:
    print(f"Ahoy, Captain! There are {len(cities_data)} wealthy settlements to go to:")
    for city_, data in cities_data.items():
        print(f"{city_} -> Population: {data['population']} citizens, Gold: {data['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
