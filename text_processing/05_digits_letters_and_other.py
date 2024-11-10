entry = input()

all_digits_found = ""
all_letters_found = ""
all_other_chars_found = ""

for char in entry:
    if char.isdigit():
        all_digits_found += char
    elif char.isalpha():
        all_letters_found += char
    elif not char.isalnum():
        all_other_chars_found += char

print(all_digits_found)
print(all_letters_found)
print(all_other_chars_found)
