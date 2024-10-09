number_sequence = input().split()
abs_numbers = []

for number in number_sequence:
    abs_numbers.append(abs(float(number)))

print(abs_numbers)