input_message = input().split()

while True:
    command = input()

    if command == "3:1":
        break

    action = command.split()[0]
    if action == "merge":
        start_index = int(command.split()[1])
        end_index = int(command.split()[2])

        if 0 <= end_index <= len(input_message) - 1:
            input_message[start_index:(end_index + 1)] = ["".join(input_message[start_index:(end_index + 1)])]
        elif start_index < 0:
            input_message[0:end_index] = ["".join(input_message[0:(end_index + 1)])]
        elif end_index > len(input_message) - 1:
            input_message[start_index:len(input_message) + 1] = ["".join(input_message[start_index:len(input_message) + 1])]

    elif action == "divide":
        counter = 0
        total_partitions = 0
        new_word = ""
        given_index = int(command.split()[1])
        partition = int(command.split()[2])
        word_to_divide = input_message[given_index]
        length_of_partitions_at_given_index = len(input_message[given_index]) // partition
        input_message.pop(given_index)
        for letter in word_to_divide:
            counter += 1
            if counter < 2 and total_partitions < partition - 1:
                new_word += letter
                continue
            if counter == 2 and total_partitions < partition - 1:
                new_word += letter
                total_partitions += 1
                input_message.append(new_word)
                counter = 0
                new_word = ""
                continue
            else:
                new_word += letter
        input_message.append(new_word)

print(" ".join(input_message))

