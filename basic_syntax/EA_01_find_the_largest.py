number = int(input())
number_str = str(number)
biggest_number = 0
current_number_str = ""
current_number = 0
#print(number_str[0])

for digit1 in range(1, int(number_str[0]) + 1):
    for digit2 in range(1, int(number_str[1]) + 1):
        for digit3 in range(1, int(number_str[2]) + 1):
            current_number_str = str(digit1) + str(digit2) + str(digit3)
            current_number = int(current_number_str)
            if current_number > biggest_number:
                biggest_number = current_number

print(biggest_number)
