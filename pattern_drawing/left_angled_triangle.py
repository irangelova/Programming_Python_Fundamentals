number_rows = int(input())

for num in range(number_rows, -1, -1):
    print("*" * num, end="")
    print()