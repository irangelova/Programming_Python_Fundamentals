count_numbers = int(input())
numbers_input = []
filtered_numbers = []

for number in range(count_numbers):
    current_number = int(input())
    numbers_input.append(current_number)

command = input()

for number in range(len(numbers_input)):
    number_to_check = numbers_input[number]
    if command == "even":
        if number_to_check % 2 == 0:
            filtered_numbers.append(number_to_check)
    elif command == "odd":
        if number_to_check % 2 != 0:
            filtered_numbers.append(number_to_check)
    elif command == "negative":
        if number_to_check < 0:
            filtered_numbers.append(number_to_check)
    elif command == "positive":
        if number_to_check >= 0:
            filtered_numbers.append(number_to_check)

print(filtered_numbers)
