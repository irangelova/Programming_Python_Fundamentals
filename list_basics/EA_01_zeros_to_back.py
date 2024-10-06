input_numbers = input().split(", ")
list_sorted = []
zeros = []

for number in input_numbers:
    if int(number) == 0:
        zeros.append(int(number))
    else:
        list_sorted.append(int(number))

list_sorted.extend(zeros)
print(list_sorted)