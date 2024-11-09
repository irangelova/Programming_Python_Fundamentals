force_side = {}
force_not_in_dict = False
user_not_in_both_sides = False
force_user_not_in_dict = True
side_changed = False

while True:
    entry = input()
    if entry == "Lumpawaroo":
        break

    if "|" in entry:
        force_not_in_dict = True
        current_force_side = entry.split(" | ")[0]
        current_force_user = entry.split(" | ")[1]
        if current_force_side not in force_side.keys():
            force_side[current_force_side] = []
            force_side[current_force_side].append(current_force_user)
            force_not_in_dict = False
        if force_not_in_dict:
            for users in force_side.values():
                user_not_in_both_sides = False
                if current_force_user not in users:
                    user_not_in_both_sides = True
            if user_not_in_both_sides:
                force_side[current_force_side].append(current_force_user)
    elif "->" in entry:
        current_force_side = entry.split(" -> ")[1]
        current_force_user = entry.split(" -> ")[0]
        if current_force_side not in force_side.keys():
            force_not_in_dict = True
        for users in force_side.values():
            user_not_in_both_sides = False
            if current_force_user in users and not side_changed:
                side_of_user = [key for key in force_side if current_force_user in force_side[key]]
                index_of_current_user = force_side[(side_of_user[0])].index(current_force_user)
                force_side[(side_of_user[0])].pop(index_of_current_user)
                force_side[current_force_side].append(current_force_user)
                force_not_in_dict = False
                user_not_in_both_sides = False
                side_changed = True
            elif current_force_user not in users and not force_not_in_dict:
                user_not_in_both_sides = True
            elif current_force_user not in users and force_not_in_dict:
                user_not_in_both_sides = True
        if user_not_in_both_sides and not force_not_in_dict:
            force_side[current_force_side].append(current_force_user)
        elif user_not_in_both_sides and force_not_in_dict:
            force_side[current_force_side] = []
            force_side[current_force_side].append(current_force_user)
        print(f"{current_force_user} joins the {current_force_side} side!")

for side in force_side.keys():
    members = len(force_side[side])
    if members > 0:
        print(f"Side: {side}, Members: {members}")
        for member in force_side[side]:
            print(f"! {member}")
