input_money_string = input().split(", ")
count_beggars = int(input())
beggars_sum = []

input_money_int = []
for element in input_money_string:
    input_money_int.append(int(element))

start_index = 0

for beggar in range(count_beggars):
    sum_current_beggar = 0
    for current_index in range(start_index, len(input_money_int), count_beggars):
        sum_current_beggar += input_money_int[current_index]
    beggars_sum.append(sum_current_beggar)
    start_index += 1

print(beggars_sum)