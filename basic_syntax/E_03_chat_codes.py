count_messages = int(input())
message = ""

for message in range(1, count_messages + 1):
    number = int(input())
    if number == 88:
        message = "Hello"
    elif number == 86:
        message = "How are you?"
    elif number < 88:
        message = "GREAT!"
    else:
        message = "Bye."
    print(message)