command = input()
coffee_needed = 0

while command != "END":
    if command == "coding" or command == "CODING" or command == "cat" \
    or command == "CAT" or command == "dog" or command == "DOG" \
    or command == "movie" or command == "MOVIE":
        if command.islower():
            coffee_needed += 1
        elif command.isupper():
            coffee_needed += 2
    command = input()

if coffee_needed > 5:
    print("You need extra sleep")
else:
    print(coffee_needed)
