number_of_lines = int(input())
sum_opening_bracket = 0
sum_closing_bracket = 0

for line in range(number_of_lines):
    text_string = input()

    if len(text_string) > 1:
        continue

    if ord(text_string) == 40:
        sum_opening_bracket += 1

    if ord(text_string) == 41:
        sum_closing_bracket += 1

if sum_opening_bracket == sum_closing_bracket:
    print("BALANCED")
else:
    print("UNBALANCED")

