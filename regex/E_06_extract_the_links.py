import re

matched_sites = []

while True:
    command = input()

    if command == "":
        break

    pattern = r"\b(www.([A-Za-z0-9\-]+)(\.[a-z]+)+)\b"
    match = re.search(pattern, command)
    if match:
        matched_sites.append(match[0])

for site in matched_sites:
    print(site)
