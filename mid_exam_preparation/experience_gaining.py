needed_experience = float(input())
count_of_battles = int(input())
current_battle = 0
total_experience = 0
experience_gained = False

for battle in range(1, count_of_battles + 1):
    current_experience_earned = float(input())
    current_battle += 1

    if battle % 3 == 0:
        current_experience_earned += 0.15 * current_experience_earned
        if battle % 5 == 0:
            current_experience_earned += 0.05 * current_experience_earned

    if battle % 5 == 0:
        current_experience_earned -= 0.1 * current_experience_earned

    total_experience += current_experience_earned

    if total_experience >= needed_experience:
        experience_gained = True
        break

if experience_gained:
    print(f"Player successfully collected his needed experience for {current_battle} battles.")
else:
    print(f"Player was not able to collect the needed experience, {(needed_experience - total_experience):.2f} more needed.")

