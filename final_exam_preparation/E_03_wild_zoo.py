animals_data = {}

while True:
    command = input().split(":")
    if command[0] == "EndDay":
        break
    elif command[0] == "Add":
        animal_name = command[1].split("-")[0]
        needed_food_quantity = int(command[1].split("-")[1])
        area = command[1].split("-")[2]
        if animal_name not in animals_data.keys():
            animals_data[animal_name] = {"needed_food": 0, "area": area}
        animals_data[animal_name]["needed_food"] += needed_food_quantity
    elif command[0] == "Feed":
        animal_name = command[1].split("-")[0]
        food_quantity = int(command[1].split("-")[1])
        if animal_name in animals_data.keys():
            animals_data[animal_name]["needed_food"] -= food_quantity
            if animals_data[animal_name]["needed_food"] <= 0:
                animals_data.pop(animal_name)
                print(f"{animal_name} was successfully fed")

print("Animals:")
for animal, data in animals_data.items():
    print(f" {animal} -> {data['needed_food']}g")

print("Areas with hungry animals:")
all_areas = []
for animal in animals_data.keys():
    areas_with_hungry_animals = animals_data[animal].get("area")
    all_areas.append(areas_with_hungry_animals)
all_areas_unique = []
for item in all_areas:
    if item not in all_areas_unique:
        all_areas_unique.append(item)
for area_with_hungry_animals in all_areas_unique:
    hungry_animals_in_area = []
    for current_animal, current_data in animals_data.items():
        if current_data["area"] == area_with_hungry_animals:
            hungry_animals_in_area.append(current_animal)
    number_of_hungry_animals_in_area = len(hungry_animals_in_area)
    print(f" {area_with_hungry_animals}: {number_of_hungry_animals_in_area}")
