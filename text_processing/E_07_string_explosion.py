entry = input()
final_string = ""
left_strength = 0

for index in range(0, len(entry)):
    if entry[index] != ">" and left_strength > 0:
        left_strength -= 1
    elif entry[index] == ">":
        final_string += entry[index]
        left_strength += int(entry[index + 1])
    else:
        final_string += entry[index]

print(final_string)
