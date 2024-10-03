factor = int(input())
count = int(input())
list_numbers = []

for number in range(1, count + 1):
    new_number = number * factor
    list_numbers.append(new_number)

print(list_numbers)