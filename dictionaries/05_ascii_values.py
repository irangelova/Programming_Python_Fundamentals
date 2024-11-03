chars = input().split(", ")
chars_dictionary = {}

for char in chars:
    key = char
    value = ord(char)
    chars_dictionary[key] = value

print(chars_dictionary)
