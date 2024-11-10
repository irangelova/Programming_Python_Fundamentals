entry = input().split()
total_sum = 0

for text in entry:
    number = int(text[1:len(text) - 1])
    previous_char = text[0]
    next_char = text[-1]
    if previous_char.isupper():
        total_sum += number / (ord(previous_char.lower()) - 96)
    elif previous_char.islower():
        total_sum += number * (ord(previous_char) - 96)
    if next_char.isupper():
        total_sum -= (ord(next_char.lower()) - 96)
    elif next_char.islower():
        total_sum += (ord(next_char.lower()) - 96)

print(f"{total_sum:.2f}")
