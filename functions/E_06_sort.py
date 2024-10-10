numbers_str = input().split()
numbers_int = []

for num in numbers_str:
    numbers_int.append(int(num))

sorted_numbers = sorted(numbers_int)
print(sorted_numbers)