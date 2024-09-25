key = int(input())
number_of_lines = int(input())

for line in range(number_of_lines):
    letter = input()
    letter_to_decrypt = ord(letter) + key
    print(chr(letter_to_decrypt), end="")