initial_message = input()
numbers_list = []
non_numbers_list = []
take_list = []
skip_list = []
result_list = []

for character in initial_message:
    if character.isdigit():
        numbers_list.append(int(character))
    else:
        non_numbers_list.append(character)

for index in range(0, len(numbers_list)):
    if index % 2 == 0:
        take_list.append(numbers_list[index])
    else:
        skip_list.append(numbers_list[index])

for take_char in take_list:
    position_skipped = False
    if take_char > len(non_numbers_list):
        result_list += non_numbers_list[0:len(non_numbers_list)]
    else:
        result_list += non_numbers_list[0:take_char]
    for char_to_remove in range(int(take_char) - 1, -1, -1):
        if char_to_remove in range(0, len(non_numbers_list)):
            non_numbers_list.pop(char_to_remove)
    if skip_list[0] > 0:
        if skip_list[0] < len(non_numbers_list):
            for skip_char_to_remove in range(int(skip_list[0]) - 1, -1, -1):
                non_numbers_list.pop(skip_char_to_remove)
    skip_list.pop(0)


print("".join(result_list))


