chars = input().split(", ")
#chars_dictionary = {}

#for char in chars:
#    key = char
#    value = ord(char)
#    chars_dictionary[key] = value

chars_dictionary = {char: ord(char) for char in chars}
print(chars_dictionary)
