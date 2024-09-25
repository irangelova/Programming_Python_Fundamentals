number_to_check = int(input())

for number in range(1, number_to_check + 1):
    sum_digits = 0
    digits = number

    while digits > 0:
        sum_digits += digits % 10
        digits = int(digits / 10)

    if (sum_digits == 5) or (sum_digits == 7) or (sum_digits == 11):
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")

