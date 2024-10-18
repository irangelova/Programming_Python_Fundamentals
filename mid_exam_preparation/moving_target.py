def shoot(targets_list: list, index: int, power: int) -> list:
    if 0 <= index <= len(targets_list) - 1:
        targets_list[index] -= power
        if targets_list[index] <= 0:
            targets_list.pop(index)
    return targets_list


def add(targets_list: list, index: int, value: int) -> list and bool:
    if 0 <= index <= len(targets_list) - 1:
        targets_list.insert(index, value)
        return targets_list, False
    else:
        return targets_list, True


def strike(targets_list: list, index: int, radius: int) -> list and str:
    if not 0 <= index <= len(targets_list) - 1:
        return targets_list, True
    for r in range(index - radius, index + radius):
        if not 0 <= r <= len(targets_list) - 1:
            return targets_list, True
    for index_ in range(index + radius, index - radius - 1, -1):
        targets_list.pop(index_)
    return targets_list, False


target_sequence = list(map(int, input().split()))
modified_targets = []
add_index_invalid = False
strike_missed = False

while True:
    command = input()

    if command == "End":
        print("|".join(list(map(str, target_sequence))))
        break

    action = command.split()[0]

    if action == "Shoot":
        current_index = int(command.split()[1])
        current_power = int(command.split()[2])
        modified_targets = shoot(target_sequence, current_index, current_power)
    elif action == "Add":
        current_index = int(command.split()[1])
        current_value = int(command.split()[2])
        modified_targets, add_index_invalid = add(target_sequence, current_index, current_value)
        if add_index_invalid:
            print("Invalid placement!")
    elif action == "Strike":
        current_index = int(command.split()[1])
        current_radius = int(command.split()[2])
        modified_targets, strike_missed = strike(target_sequence, current_index, current_radius)
        if strike_missed:
            print("Strike missed!")


