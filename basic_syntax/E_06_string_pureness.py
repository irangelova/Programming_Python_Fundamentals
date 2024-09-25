count_strings = int(input())

for string in range(1, count_strings + 1):
    given_string = input()
    if "," in given_string or "." in given_string or "_" in given_string:
        print(f"{given_string} is not pure!")
    else:
        print(f"{given_string} is pure.")