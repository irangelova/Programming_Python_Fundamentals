text = input()
new_password = ""

while True:
    command = input().split()
    if command[0] == "Done":
        break
    elif command[0] == "TakeOdd":
        for index in range(len(text)):
            if index % 2 != 0:
                new_password += text[index]
        print(new_password)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        substring = new_password[index:(index + length)]
        new_password = new_password.replace(substring, "", 1)
        print(new_password)
    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in new_password:
            new_password = new_password.replace(substring, substitute)
            print(new_password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {new_password}")
