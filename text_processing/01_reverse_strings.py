while True:
    entry = input()
    if entry == "end":
        break

    reversed_entry = entry[::-1]
    print(f"{entry} = {reversed_entry}")