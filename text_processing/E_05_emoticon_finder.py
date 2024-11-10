message = input()

#for char in range(0, len(message)):
#    if message[char] == ":":
#        print(f"{message[char]}{message[char + 1]}")

emoticons = [(message[char] + message[char + 1]) for char in range(0, len(message)) if message[char] == ":"]
print("\n".join(emoticons))
