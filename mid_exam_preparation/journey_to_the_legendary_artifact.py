initial_energy = float(input())
count_of_mountains = 0
artifacts_found = 0
all_artifacts_found = False
energy_used_up = False

while True:
    terrain = input()

    if terrain == "Journey ends here!":
        break
    if terrain == "mountain":
        if initial_energy < 10:
            energy_used_up = True
            break
        else:
            initial_energy -= 10
        count_of_mountains += 1
        if count_of_mountains % 3 == 0:
            artifacts_found += 1
            if artifacts_found == 3:
                all_artifacts_found = True
                break
    if terrain == "desert":
        if initial_energy < 15:
            energy_used_up = True
            break
        else:
            initial_energy -= 15
    if terrain == "forest":
        initial_energy += 7

    if initial_energy == 0:
        print("The character is too exhausted to carry on with the journey.")
        break

if all_artifacts_found:
    print(f"The character reached the legendary artifact with {initial_energy:.2f} energy left.")
elif energy_used_up:
    print("The character is too exhausted to carry on with the journey.")
else:
    print(f"The character could not find all the pieces and needs {3 - artifacts_found} more to complete the legendary artifact.")