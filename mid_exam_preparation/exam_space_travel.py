def travel(light_years: int, fuel: int) -> int and bool:
    if fuel >= light_years:
        fuel -= light_years
        return fuel, True
    else:
        return fuel, False


def enemy(armour: int, ammo: int, fuel: int) -> int and str:
    if ammo >= armour:
        ammo -= armour
        message = f"An enemy with {armour} armour is defeated."
        return ammo, fuel, message
    elif fuel >= 2 * armour:
        fuel -= 2 * armour
        message = f"An enemy with {armour} armour is outmaneuvered."
        return ammo, fuel, message
    else:
        message = "Mission failed."
        return ammo, fuel, message


travel_route = input().split("||")
initial_fuel = int(input())
initial_ammo = int(input())
distance_traveled = False
enemy_message = ""

for route in travel_route:
    command = route.split()[0]

    if command == "Travel":
        light_years_traveled = int(route.split()[1])
        initial_fuel, distance_traveled = travel(light_years_traveled, initial_fuel)
        if distance_traveled:
            print(f"The spaceship travelled {light_years_traveled} light-years.")
        else:
            print("Mission failed.")
            break
    elif command == "Enemy":
        enemy_armour = int(route.split()[1])
        initial_ammo, initial_fuel, enemy_message = enemy(enemy_armour, initial_ammo, initial_fuel)
        print(enemy_message)
        if enemy_message == "Mission failed.":
            break
    elif command == "Repair":
        value_added = int(route.split()[1])
        initial_fuel += value_added
        initial_ammo += 2 * value_added
        print(f"Ammunitions added: {2 * value_added}.")
        print(f"Fuel added: {value_added}.")
    elif command == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break

