input_names = input().split(", ")

sorted_list = sorted(input_names, key=lambda x: (-len(x), x))

print(sorted_list)
