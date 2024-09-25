animals = input()
animals_list = list(animals.split(", "))
counter_animals = len(animals_list)

if animals_list[len(animals_list)-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for animal in animals_list:
        counter_animals -= 1
        if animal == "wolf":
            print(f"Oi! Sheep number {counter_animals}! You are about to be eaten by a wolf!")
            break
