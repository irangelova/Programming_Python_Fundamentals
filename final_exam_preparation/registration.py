def create_username():
    username = input()
    reversed_string = ""

    while True:
        command = input().split()

        if command[0] == "Registration":
            break
        elif command[0] == "Letters":
            case = command[1]
            if case == "Lower":
                username = username.lower()
            elif case == "Upper":
                username = username.upper()
            print(username)
        elif command[0] == "Reverse":
            start_index, end_index = int(command[1]), int(command[2])
            if start_index in range(len(username)) and (end_index + 1) in range(len(username)):
                reversed_string = username[start_index:end_index + 1]
                reversed_string = reversed_string[::-1]
            print(reversed_string)
        elif command[0] == "Substring":
            substring = command[1]
            if substring in username:
                username = username.replace(substring, "")
                print(username)
            else:
                print(f"The username {username} doesn't contain {substring}.")
        elif command[0] == "Replace":
            char = command[1]
            username = username.replace(char, "-")
            print(username)
        elif command[0] == "IsValid":
            char = command[1]
            if char in username:
                print("Valid username.")
            else:
                print(f"{char} must be contained in your username.")


create_username()
