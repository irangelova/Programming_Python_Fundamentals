new_string = ""

while True:
    command = input()

    if command == "End":
        break

    if command != "SoftUni":
        for letter in command:
            new_string += letter * 2
        print(new_string)

    new_string = ""
