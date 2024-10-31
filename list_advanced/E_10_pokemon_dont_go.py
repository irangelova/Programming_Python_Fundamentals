input_sequence = input().split()
sum_removed_elements = 0

while True:
    current_index = int(input())
    current_removed_value = 0

    if current_index < 0:
        sum_removed_elements += int(input_sequence[0])
        current_removed_value = int(input_sequence[0])
        input_sequence.pop(0)
        last_element = input_sequence[-1]
        input_sequence.insert(0, last_element)
    elif current_index > len(input_sequence) - 1:
        sum_removed_elements += int(input_sequence[-1])
        current_removed_value = int(input_sequence[-1])
        input_sequence.pop()
        first_element = input_sequence[0]
        input_sequence.insert(len(input_sequence), first_element)

    elif 0 <= current_index <= len(input_sequence) - 1:
        sum_removed_elements += int(input_sequence[current_index])
        current_removed_value = int(input_sequence[current_index])
        input_sequence.pop(current_index)
    new_sequence = []
    for number in input_sequence:
        if int(number) <= current_removed_value:
            new_sequence.append(int(number) + current_removed_value)
        else:
            new_sequence.append(int(number) - current_removed_value)
    input_sequence = new_sequence
    if len(input_sequence) == 0:
        break

print(sum_removed_elements)