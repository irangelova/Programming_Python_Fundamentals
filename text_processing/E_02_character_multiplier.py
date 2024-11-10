entry = input().split()
total_sum = 0

len_first_string = len(entry[0])
len_second_string = len(entry[1])

if len_first_string == len_second_string:
    for char in range(0, len_first_string):
        total_sum += ord(entry[0][char]) * ord(entry[1][char])
elif len_first_string > len_second_string:
    for char in range(0, len_second_string):
        total_sum += ord(entry[0][char]) * ord(entry[1][char])
    for char in range(len_second_string, len_first_string):
        total_sum += ord(entry[0][char])
else:
    for char in range(0, len_first_string):
        total_sum += ord(entry[0][char]) * ord(entry[1][char])
    for char in range(len_first_string, len_second_string):
        total_sum += ord(entry[1][char])

print(total_sum)
