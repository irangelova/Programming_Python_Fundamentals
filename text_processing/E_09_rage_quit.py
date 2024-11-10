entry = input()
final_string = ""
string_to_repeat = ""
count_repeat = ""

for index in range(len(entry)):
    if not entry[index].isdigit():
        string_to_repeat += entry[index].upper()
    else:
        for next_char in range(index, len(entry)):
            if not entry[next_char].isdigit():
                break
            count_repeat += entry[next_char]
        final_string += string_to_repeat * int(count_repeat)
        string_to_repeat = ""
        count_repeat = ""

print(f"Unique symbols used: {len(set(final_string))}")
print(final_string)
