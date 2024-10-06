number_sequence = input().split()
input_string = input()
string_list = list(input_string)

for sequence in number_sequence:
    sum_numbers = 0
    for number in sequence:
        sum_numbers += int(number)
    len_string = len(string_list)
    current_letter = string_list[sum_numbers % len_string]
    string_list.remove(current_letter)
    print(current_letter, end="")
