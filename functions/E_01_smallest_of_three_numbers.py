def find_smallest(number1: int, number2: int, number3: int) -> int:
    numbers_to_check = [number1, number2, number3]
    smallest_number = min(numbers_to_check)
    return smallest_number


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(find_smallest(first_number, second_number, third_number))