count_rows = int(input())

for row in range(count_rows):
    print(" " * (count_rows - row) + "*" * (2 * row + 1))