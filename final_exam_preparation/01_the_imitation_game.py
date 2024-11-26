def encrypt_message():
    message = input()

    while True:
        command = input().split("|")
        if command[0] == "Decode":
            break
        elif command[0] == "Move":
            number_of_letters = int(command[1])
            message = message[number_of_letters:] + message[:number_of_letters]
        elif command[0] == "Insert":
            index = int(command[1])
            value = command[2]
            message = message[:index] + value + message[index:]
        elif command[0] == "ChangeAll":
            substring = command[1]
            replacement = command[2]
            message = message.replace(substring, replacement)

    print(f"The decrypted message is: {message}")


encrypt_message()
