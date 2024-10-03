gift_names = input().split()
#print(gift_names)
#command = input().split()
#print(command)
index = 0

while True:
    command_string = input().split()
    command = command_string[0]
    gift = command_string[1]
    if len(command_string) == 3:
        index = int(command_string[2])
    if command == "OutOfStock":
        for index, current_gift in enumerate(gift_names):
            if current_gift == gift:
                gift_names[index] = "None"
    elif command == "Required" and 0 < index <= len(gift_names)-1:
        gift_names[index] = gift
    elif command == "JustInCase":
        gift_names[-1] = gift
    elif command == "No":
        break

for final_gift in gift_names:
    if final_gift != "None":
        print(final_gift, end=" ")
