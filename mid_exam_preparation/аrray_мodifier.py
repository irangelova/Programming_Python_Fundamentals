def swap(the_array: list, index1: int, index2: int) -> list:
    the_array[index1], the_array[index2] = the_array[index2], the_array[index1]
    return the_array


def multiply(the_array: list, index1: int, index2: int) -> list:
    array_with_ints = list(map(int, the_array))
    product = array_with_ints[index1] * array_with_ints[index2]
    the_array.pop(index1)
    the_array.insert(index1, product)
    return list(map(str, array_with_ints))


def decrease(the_array: list) -> list:
    new_array = list(map(int, the_array))
    for element in range(len(new_array)):
        new_array[element] -= 1
    return list(map(str, new_array))


initial_array = input().split()
modified_array = []

while True:
    command = input()

    if command == "end":
        break

    action = command.split()[0]
    if action == "swap":
        first_index = int(command.split()[1])
        second_index = int(command.split()[2])
        modified_array = swap(initial_array, first_index, second_index)
    elif action == "multiply":
        first_index = int(command.split()[1])
        second_index = int(command.split()[2])
        modified_array = multiply(initial_array, first_index, second_index)
    elif action == "decrease":
        modified_array = decrease(initial_array)
    else:
        break

print(", ".join(modified_array))

