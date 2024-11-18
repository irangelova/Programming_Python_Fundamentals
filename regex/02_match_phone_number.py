import re

phone_numbers = input()
pattern = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"
matches = re.findall(pattern, phone_numbers)

for index in range(len(matches)):
    if index < len(matches) - 1:
        print(matches[index], end=", ")
    else:
        print(matches[index])
