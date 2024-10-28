input_string = input()
vowels = ['a', 'o', 'u', 'e', 'i']

list_without_vowels = [letter for letter in input_string if letter.lower() not in vowels]

print("".join(list_without_vowels))