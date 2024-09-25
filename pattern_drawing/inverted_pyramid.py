count_rows = int(input())

for row in range(count_rows - 1, -1, -1):
    print(" " * (count_rows - row) + "*" * (2 * row + 1))