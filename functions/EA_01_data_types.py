def data_type_check(type: str, message: str):
    if type == "string":
        return f"${message}$"
    elif type == "int":
        return int(message) * 2
    elif type == "real":
        new_message = float(message) * 1.5
        return f"{new_message:.2f}"


message_type = input()
message_to_check = input()
print(data_type_check(message_type, message_to_check))
