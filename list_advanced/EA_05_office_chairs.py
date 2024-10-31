number_of_rooms = int(input())
total_free_chairs = 0
chairs_sufficient = False

for room in range(1, number_of_rooms + 1):
    information = input().split()
    chairs = information[0]
    people = int(information[1])
    if len(chairs) < people:
        print(f"{people - len(chairs)} more chairs needed in room {room}")
    total_free_chairs += len(chairs) - people

if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")
