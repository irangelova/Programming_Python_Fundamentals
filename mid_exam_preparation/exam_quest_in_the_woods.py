days_of_adventures = int(input())
number_adventurers = int(input())
initial_group_energy = float(input())
daily_water_per_person = float(input())
daily_food_per_person = float(input())
energy_used = False

total_water_supply_needed = days_of_adventures * number_adventurers * daily_water_per_person
total_food_supply_needed = days_of_adventures * number_adventurers * daily_food_per_person

for day in range(1, days_of_adventures + 1):
    daily_energy_loss = float(input())

    initial_group_energy -= daily_energy_loss
    if initial_group_energy <= 0:
        energy_used = True
        break

    if day % 2 == 0:
        initial_group_energy += 0.05 * initial_group_energy
        total_water_supply_needed = total_water_supply_needed * 0.7

    if day % 3 == 0:
        initial_group_energy += 0.1 * initial_group_energy
        total_food_supply_needed -= (total_food_supply_needed / number_adventurers)

if energy_used:
    print(f"You will run out of energy. You will be left with {total_food_supply_needed:.2f} food and {total_water_supply_needed:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with {initial_group_energy:.2f} energy!")
