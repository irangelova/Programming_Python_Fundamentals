command_counter = 0
current_resource = ""
resource_dictionary = {}

while True:
    command = input()

    if command == "stop":
        break

    command_counter += 1

    if command_counter % 2 != 0:
        current_resource = command
        if current_resource not in resource_dictionary.keys():
            resource_dictionary[current_resource] = 0
    elif command_counter % 2 == 0:
        resource_dictionary[current_resource] += int(command)

for resource, quantity in resource_dictionary.items():
    print(f"{resource} -> {quantity}")
