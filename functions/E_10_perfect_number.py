def is_perfect(number: int) -> str:
    sum_digits = 0
    for digit in range(1, number):
        if number % digit == 0:
            sum_digits += digit
    if sum_digits == number:
        return "We have a perfect number!"
    return "It's not so perfect."


number_to_check = int(input())
print(is_perfect(number_to_check))
