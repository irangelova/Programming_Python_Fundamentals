number_input = input().split()

list_numbers = []

for number in number_input:
    opposite_number = int(number) * -1
    list_numbers.append(opposite_number)

print(list_numbers)