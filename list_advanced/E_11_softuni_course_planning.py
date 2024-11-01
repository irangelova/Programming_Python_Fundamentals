initial_schedule = input().split(", ")
position = 1

while True:
    command = input()
    if command == "course start":
        break

    action = command.split(":")[0]

    if action == "Add":
        lesson_title = command.split(":")[1]
        if lesson_title not in initial_schedule:
            initial_schedule.append(lesson_title)
    elif action == "Insert":
        lesson_title = command.split(":")[1]
        index_to_insert = int(command.split(":")[2])
        if lesson_title not in initial_schedule:
            initial_schedule.insert(index_to_insert, lesson_title)
    elif action == "Remove":
        lesson_title = command.split(":")[1]
        if lesson_title in initial_schedule:
            title_index = initial_schedule.index(lesson_title)
            if title_index + 1 in range(len(initial_schedule)):
                if "Exercise" in initial_schedule[title_index + 1]:
                    initial_schedule.pop(initial_schedule.index(lesson_title) + 1)
            initial_schedule.remove(lesson_title)
    elif action == "Swap":
        lesson_title1 = command.split(":")[1]
        lesson_title2 = command.split(":")[2]
        if lesson_title1 in initial_schedule and lesson_title2 in initial_schedule:
            lesson1_index = initial_schedule.index(lesson_title1)
            lesson2_index = initial_schedule.index(lesson_title2)
            exercise1_in_list = False
            exercise2_in_list = False
            if lesson1_index + 1 in range(len(initial_schedule)):
                exercise1_in_list = "Exercise" in initial_schedule[lesson1_index + 1]
            if lesson2_index + 1 in range(len(initial_schedule)):
                exercise2_in_list = "Exercise" in initial_schedule[lesson2_index + 1]
            initial_schedule[lesson1_index], initial_schedule[lesson2_index] = initial_schedule[lesson2_index], \
                                                                               initial_schedule[lesson1_index]
            if exercise1_in_list and exercise2_in_list:
                initial_schedule[lesson1_index + 1], initial_schedule[lesson2_index + 1] = \
                initial_schedule[lesson2_index + 1], initial_schedule[lesson1_index + 1]
            elif not exercise1_in_list and exercise2_in_list:
                initial_schedule.insert(lesson1_index + 1, initial_schedule.pop(lesson2_index + 1))
            elif exercise1_in_list and not exercise2_in_list:
                initial_schedule.insert(lesson2_index + 1, initial_schedule.pop(lesson1_index + 1))

    elif action == "Exercise":
        lesson_title = command.split(":")[1]
        if lesson_title in initial_schedule and f"{lesson_title}-Exercise" not in initial_schedule:
            initial_schedule.insert(initial_schedule.index(lesson_title) + 1, f"{lesson_title}-Exercise")
        elif lesson_title not in initial_schedule:
            initial_schedule.append(lesson_title)
            initial_schedule.append(f"{lesson_title}-Exercise")

for lesson in initial_schedule:
    print(f"{position}.{lesson}")
    position += 1




