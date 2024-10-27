integer_sequence = input().split()

while True:
    command = input()

    if command == "END":
        break

    length_command = len(command.split())
    action1 = command.split()[0]
    action2 = command.split()[1]

    if action1 == "add":
        for number in range(length_command - 1, 2, -1):
            integer_to_add = command.split()[number]
            integer_sequence.insert(0, integer_to_add)
    elif action1 == "remove" and action2 != "at":
        value_to_compare = int(command.split()[3])
        for number in range(len(integer_sequence) - 1, -1, -1):
            if int(integer_sequence[number]) > value_to_compare:
                integer_sequence.pop(int(number))
            else:
                integer_sequence = integer_sequence
    elif action1 == "replace":
        value_to_find = action2
        replacement = command.split()[2]
        if value_to_find not in integer_sequence:
            integer_sequence = integer_sequence
        else:
            for number in integer_sequence:
                if int(number) == int(value_to_find):
                    index_to_replace = integer_sequence.index(number)
                    integer_sequence[index_to_replace] = replacement
                    break
    elif action1 == "remove" and action2 == "at":
        given_index = int(command.split()[3])
        if 0 <= given_index < len(integer_sequence) + 1:
            integer_sequence.pop(given_index)
        else:
            integer_sequence = integer_sequence
    elif action1 == "find" and action2 == "even":
        for number in integer_sequence:
            if int(number) % 2 == 0:
                print(number, end=" ")
    elif action1 == "find" and action2 == "odd":
        for number in integer_sequence:
            if int(number) % 2 != 0:
                print(number, end=" ")


print()
print(", ".join(integer_sequence))
