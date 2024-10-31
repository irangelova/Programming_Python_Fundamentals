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
            input_message[start_index:end_index] = ["".join(input_message[start_index:end_index])]
        else:
            input_message[start_index:(len(input_message) - 1)] = ["".join(input_message[start_index:(len(input_message) - 1)])]
    elif action == "divide":
        given_index = int(command.split()[1])
        partition = int(command.split()[2])
        length_of_partitions_at_given_index = len(input_message[given_index]) // partition
        start_index = 0
        for part in range(1, partition + 1):
            if part == (partition + 1) and len(input_message[given_index]) % partition != 0:
                current_part = input_message[given_index][start_index:]
            else:
                current_part = input_message[given_index][start_index:(start_index + length_of_partitions_at_given_index)]
                start_index += length_of_partitions_at_given_index

print(" ".join(input_message))


