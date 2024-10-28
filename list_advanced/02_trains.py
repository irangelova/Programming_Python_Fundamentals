train_list = [0] * int(input())

while True:
    command = input()

    if command == "End":
        break

    action = command.split()[0]
    if action == "add":
        people_to_add = int(command.split()[1])
        train_list[-1] += people_to_add
    elif action == "insert":
        given_index = int(command.split()[1])
        people_to_insert = int(command.split()[2])
        train_list[given_index] += people_to_insert
    elif action == "leave":
        given_index = int(command.split()[1])
        people_to_leave = int(command.split()[2])
        train_list[given_index] -= people_to_leave

print(train_list)