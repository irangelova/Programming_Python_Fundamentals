import re

number_of_messages = int(input())
pattern = r"\B(\$|%)([A-Z][a-z]{2,})\1:\s\[([0-9]+)\]\|\[([0-9]+)\]\|\[([0-9]+)\]\|$"

for number in range(number_of_messages):
    message = input()
    match = re.findall(pattern, message)

    if match:
        decrypted_message = ""
        for index in range(2, 5):
            decrypted_message += chr(int(match[0][index]))
        print(f"{match[0][1]}: {decrypted_message}")
    else:
        print("Valid message not found!")
