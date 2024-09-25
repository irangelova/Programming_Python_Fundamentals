number_rows = int(input())

for row in range((number_rows // 2) + 1):
    print(" " * (number_rows - row - 1) + "*" * (2 * row + 1))
for row in range((number_rows // 2 - 1), -1, -1):
    print(" " * (number_rows - row - 1) + "*" * (2 * row + 1))