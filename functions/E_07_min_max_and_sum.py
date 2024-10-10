numbers_str = input().split()
numbers_int = []

for num in numbers_str:
    numbers_int.append(int(num))

min_number = min(numbers_int)
max_number = max(numbers_int)
sum_numbers = sum(numbers_int)

print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_numbers}")

