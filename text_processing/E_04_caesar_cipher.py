message = input()

#for char in message:
#    new_char = chr(ord(char) + 3)
#    print(new_char, end="")

encrypted_message = [chr(ord(char) + 3) for char in message]
print("".join(encrypted_message))
