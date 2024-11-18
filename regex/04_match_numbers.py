import re

numbers = input()
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
matching_numbers = re.finditer(pattern, numbers)

for match in matching_numbers:
    print(match.group(), end=" ")
