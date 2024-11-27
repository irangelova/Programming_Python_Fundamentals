number_of_lines = int(input())
plants = {}
invalid_plant_name = False

for line in range(number_of_lines):
    plant_data = input().split("<->")
    if plant_data[0] not in plants.keys():
        plants[plant_data[0]] = {}
    plants[plant_data[0]] = {"rarity": plant_data[1], "rating": []}

while True:
    command = input().split(": ")
    if command[0] == "Exhibition":
        break
    elif command[0] == "Rate":
        plant = command[1].split(" - ")[0]
        rating = int(command[1].split(" - ")[1])
        if plant not in plants.keys():
            print("error")
        else:
            plants[plant]["rating"].append(rating)
    elif command[0] == "Update":
        plant = command[1].split(" - ")[0]
        new_rarity = command[1].split(" - ")[1]
        if plant not in plants.keys():
            print("error")
        else:
            plants[plant]["rarity"] = new_rarity
    elif command[0] == "Reset":
        plant = command[1]
        if plant not in plants.keys():
            print("error")
        else:
            plants[plant]["rating"].clear()

print("Plants for the exhibition:")
for plant_name, data in plants.items():
    if len(data['rating']) == 0:
        average_rating = 0
    else:
        average_rating = sum(data['rating'])/len(data['rating'])
    print(f"- {plant_name}; Rarity: {data['rarity']}; Rating: {average_rating:.2f}")
