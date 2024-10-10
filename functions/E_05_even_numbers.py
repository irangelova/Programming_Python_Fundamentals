current_numbers_str = input().split()
current_numbers_int = []

for num in current_numbers_str:
    current_numbers_int.append(int(num))

is_even = lambda number: number % 2 == 0
even_numbers = list(filter(is_even, current_numbers_int))
print(even_numbers)

