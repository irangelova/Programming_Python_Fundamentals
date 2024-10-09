def even_odd_sum(number: str) -> str:
    sum_even = sum_odd = 0
    for digit in number:
        if int(digit) % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)
    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"


current_number = input()
print(even_odd_sum(current_number))