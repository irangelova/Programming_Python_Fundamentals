usernames = input().split(", ")
valid_usernames = []

for username in usernames:
    username_valid = False
    if 3 <= len(username) <= 16:
        username_valid = True
    if username_valid:
        for char in username:
            if not(char.isalpha() or char.isdigit() or char == "-" or char == "_") or char.isspace():
                username_valid = False
                break

    if username_valid:
        valid_usernames.append(username)

print("\n".join(valid_usernames))
