parking_lot_dictionary = {}
number_of_commands = int(input())


def register(parking: dict, username: str, license_plate: str) -> str:
    if username in parking.keys():
        return f"ERROR: already registered with plate number {license_plate}"
    parking[username] = license_plate
    return f"{username} registered {license_plate} successfully"


def unregister(parking: dict, username: str):
    if username not in parking.keys():
        return f"ERROR: user {username} not found"
    parking.pop(username)
    return f"{username} unregistered successfully"


for command in range(number_of_commands):
    current_command = input().split()

    if current_command[0] == "register":
        current_username = current_command[1]
        current_license_plate = current_command[2]
        result = register(parking_lot_dictionary, current_username, current_license_plate)
        print(result)
    elif current_command[0] == "unregister":
        current_username = current_command[1]
        result = unregister(parking_lot_dictionary, current_username)
        print(result)

for user, plate in parking_lot_dictionary.items():
    print(f"{user} => {plate}")
