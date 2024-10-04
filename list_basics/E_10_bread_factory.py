input_events = input().split("|")
initial_energy = 100
initial_coins = 100
gained_energy = 0
orders_managed = 0
current_energy = initial_energy
bakery_open = True

for event in range(len(input_events)):
    current_event = (input_events[event]).split("-")
    event_name = current_event[0]
    event_number = int(current_event[1])

    if event_name == "rest":
        initial_energy = current_energy
        current_energy += event_number
        if current_energy > 100:
            current_energy = 100
        gained_energy = current_energy - initial_energy
        orders_managed += 1
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {current_energy}.")

    elif event_name == "order":
        if current_energy >= 30:
            current_energy -= 30
            initial_coins += event_number
            print(f"You earned {event_number} coins.")
            orders_managed += 1
        else:
            current_energy += 50
            print(f"You had to rest!")
    else:
        if initial_coins >= event_number:
            initial_coins -= event_number
            print(f"You bought {event_name}.")
            orders_managed += 1
        else:
            print(f"Closed! Cannot afford {event_name}.")
            bakery_open = False
            break

if bakery_open:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {current_energy}")
