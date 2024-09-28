number_of_lines = int(input())
sum_opening_bracket = 0
bracket_opened = False

for line in range(number_of_lines):
    text_string = input()

    if len(text_string) > 1:
        continue

    if ord(text_string) == 40:
        sum_opening_bracket += 1
        bracket_opened = True
        if sum_opening_bracket > 1:
            break

    if ord(text_string) == 41:
        sum_opening_bracket -= 1
        bracket_opened = False
        if sum_opening_bracket < 0:
            break

if sum_opening_bracket == 0 and bracket_opened is False:
    print("BALANCED")
else:
    print("UNBALANCED")


