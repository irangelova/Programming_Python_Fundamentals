year_input = int(input())

while True:
    year_input += 1
    year_to_check = str(year_input)

    if len(set(year_to_check)) == len(year_to_check):
        break

print(year_input)
