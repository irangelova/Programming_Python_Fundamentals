sequence = input().split()
dictionary = {}

for element in sequence:
    element_lower = element.lower()
    if element_lower not in dictionary:
        dictionary[element_lower] = 0
    dictionary[element_lower] += 1

for (key, value) in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")
