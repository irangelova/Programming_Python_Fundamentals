def round_numbers(number):
    return round(number)


numbers_to_round = input().split()
rounded_numbers = []

for num in numbers_to_round:
    rounded_number = round_numbers(float(num))
    rounded_numbers.append(rounded_number)

print(rounded_numbers)
