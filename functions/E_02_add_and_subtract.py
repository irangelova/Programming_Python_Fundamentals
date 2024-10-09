def sum_numbers(number1: int, number2: int) -> int:
    sum_of_numbers = number1 + number2
    return sum_of_numbers


def subtract(calculated_sum, number3):
    difference = calculated_sum - number3
    return difference


def add_and_subtract(num1, num2, num3):
    current_sum = sum_numbers(num1, num2)
    current_difference = subtract(current_sum, num3)
    return current_difference


first_number = int(input())
second_number = int(input())
third_number = int(input())
result = add_and_subtract(first_number, second_number, third_number)
print(result)
