def is_even(number: str):
    if int(number) % 2 == 0:
        return True
    else:
        return False


current_numbers = input().split()
even_numbers = list(filter(is_even, current_numbers))

print(even_numbers)

