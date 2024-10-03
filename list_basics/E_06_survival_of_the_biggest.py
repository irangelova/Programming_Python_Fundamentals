numbers_str = input().split()
numbers_to_remove = int(input())
numbers_int = []
left_numbers_string = []
numbers_left = []

for number in numbers_str:
    numbers_int.append(int(number))

for del_number in range(numbers_to_remove):
    numbers_int.remove(min(numbers_int))

for int_number in numbers_int:
    left_numbers_string.append(str(int_number))
numbers_left = ", ".join(left_numbers_string)

print(numbers_left)

