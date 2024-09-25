count_rows = int(input())

for row in range(1, count_rows + 1):
    number_to_print = ""
    for number in range(1, row + 1):
        number_to_print += str(number)
    print(number_to_print)
