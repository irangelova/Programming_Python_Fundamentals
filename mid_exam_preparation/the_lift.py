people_waiting = int(input())
lifts_state = list(map(int, input().split()))

for wagon in range(len(lifts_state)):
    free_seats = 4 - lifts_state[wagon]

    if people_waiting >= free_seats:
        lifts_state[wagon] += free_seats
        people_waiting -= free_seats
    else:
        lifts_state[wagon] += people_waiting
        people_waiting = 0

    if people_waiting == 0:
        break

if people_waiting == 0 and any(seats < 4 for seats in lifts_state):
    print("The lift has empty spots!")
    print(" ".join(map(str, lifts_state)))
elif people_waiting > 0 and all(seats == 4 for seats in lifts_state):
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(" ".join(map(str, lifts_state)))
else:
    print(" ".join(map(str, lifts_state)))


