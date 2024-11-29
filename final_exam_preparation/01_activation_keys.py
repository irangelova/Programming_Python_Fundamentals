raw_activation_key = input()

while True:
    command = input().split(">>>")
    if command[0] == "Generate":
        break
    elif command[0] == "Contains":
        substring = command[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        case = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        substring_to_change = raw_activation_key[start_index:end_index]
        if case == "Upper":
            substring_to_change = substring_to_change.upper()
        else:
            substring_to_change = substring_to_change.lower()
        raw_activation_key = raw_activation_key[:start_index] + substring_to_change + raw_activation_key[end_index:]
        print(raw_activation_key)
    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)

print(f"Your activation key is: {raw_activation_key}")
