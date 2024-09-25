word = input()
uppercase_index = -1
uppercase_letter = []

for letter in word:
    uppercase_index += 1
    if letter.isupper():
        uppercase_letter.append(uppercase_index)

print(uppercase_letter)
