import re
matched_numbers = []

while True:
    command = input()

    if command == "":
        break

    pattern = r"\d+"
    matches = re.findall(pattern, command)
    matched_numbers += matches

print(" ".join(matched_numbers))
