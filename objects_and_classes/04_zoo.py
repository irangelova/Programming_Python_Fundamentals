class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species: str, name: str):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {self.__animals}"
        elif species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {self.__animals}"
        elif species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {self.__animals}"


name_of_zoo = input()
zoo = Zoo(name_of_zoo)
number_of_lines = int(input())

for line in range(number_of_lines):
    animal = input().split()
    animal_species = animal[0]
    animal_name = animal[1]
    zoo.add_animal(animal_species, animal_name)

species_to_print = input()
print(zoo.get_info(species_to_print))

