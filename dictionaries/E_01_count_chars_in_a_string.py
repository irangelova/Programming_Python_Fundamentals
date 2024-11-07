message = input()
char_dictionary = {}

for char in message:
    if char not in char_dictionary.keys() and char != " ":
        char_dictionary[char] = 1
    elif char in char_dictionary.keys() and char != " ":
        char_dictionary[char] += 1

for key, value in char_dictionary.items():
    print(f"{key} -> {value}")
