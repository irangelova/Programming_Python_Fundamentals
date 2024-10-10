def factorial(number1: int, number2: int) -> str:
    for num1 in range(1, number1):
        number1 *= num1
    for num2 in range(1, number2):
        number2 *= num2
    final_result = number1 / number2
    return f"{final_result:.2f}"


first_number = int(input())
second_number = int(input())
print(factorial(first_number, second_number))
