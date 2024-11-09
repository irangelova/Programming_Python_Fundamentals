force_side_dictionary = {}

while True:
    entry = input()
    if entry == "Lumpawaroo":
        break

    if "|" in entry:
        force_side,force_user = entry.split(" | ")
        user_is_part_of_the_force = False
        for force_side_users in force_side_dictionary.values():
            if force_user in force_side_users:
                user_is_part_of_the_force = True
                break
        if not user_is_part_of_the_force:
            if force_side not in force_side_dictionary.keys():
                force_side_dictionary[force_side] = []
            force_side_dictionary[force_side].append(force_user)
    elif "->" in entry:
        force_user, force_side = entry.split(" -> ")
        for force_side_users in force_side_dictionary.values():
            if force_user in force_side_users:
                force_side_users.remove(force_user)
                break
        if force_side not in force_side_dictionary.keys():
            force_side_dictionary[force_side] = []
        force_side_dictionary[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
for force_side, force_users in force_side_dictionary.items():
    if len(force_users) > 0:
        print(f"Side: {force_side}, Members: {len(force_users)}")
        for force_user in force_users:
            print(f"! {force_user}")
