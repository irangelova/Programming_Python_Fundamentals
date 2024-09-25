square_size = int(input())
row = 1

for num in range(1, square_size + 1):
    if row == 1 or row == square_size:
        print("*"*square_size)
        row += 1
    else:
        print("*", end="")
        print(" "*(square_size - 2), end="")
        print("*", end="")
        row += 1
        print()
