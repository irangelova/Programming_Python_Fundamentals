targets_list = list(map(int, input().split()))
shot_targets = 0
last_target_shot = 0

while True:
    command = input()

    if command == "End":
        print(f"Shot targets: {shot_targets} -> {' '.join(list(map(str, targets_list)))}")
        break

    index = int(command)

    if 0 <= index <= len(targets_list) - 1:
        if targets_list[index] != -1:
            last_target_shot = targets_list[index]
            targets_list[index] = -1
            shot_targets += 1
        for element in range(len(targets_list)):
            if targets_list[element] > last_target_shot and targets_list[element] != -1:
                targets_list[element] -= last_target_shot
            elif targets_list[element] <= last_target_shot and targets_list[element] != -1:
                targets_list[element] += last_target_shot
    else:
        targets_list = targets_list


