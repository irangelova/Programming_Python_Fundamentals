first_string = input()
second_string = input()
new_string = ""
previous_string = first_string

for letter in range(len(first_string)):
    left_part = second_string[:letter + 1]
    right_part = first_string[letter + 1:]
    new_string = left_part + right_part
    if previous_string != new_string:
        print(new_string)
    previous_string = new_string
