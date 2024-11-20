import re

text = input()
pattern = r"\s((([a-z0-9]+)[a-z0-9\.\-\_]*)@([a-z-]+)(\.[a-z]+)+)\b"
valid_emails = re.findall(pattern, text)

for email in valid_emails:
    print(email[0])
