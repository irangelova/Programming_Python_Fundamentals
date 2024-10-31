from math import ceil

input_numbers = list(map(int, input().split(", ")))
max_number = max(input_numbers)
number_of_groups = ceil(max_number / 10)

for group in range(1, number_of_groups + 1):
    current_group = []
    for number in input_numbers:
        if ((group * 10) - 10) < number <= (group * 10):
            current_group.append(number)
    print(f"Group of {group * 10}'s: {current_group}")
