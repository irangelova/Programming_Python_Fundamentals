students = []
course_to_show = ""

while True:
#    command = input()
    command = input().split(":")

    if len(command) == 1:
        course_to_show = command
        break
#    if ":" not in command:
#        course_to_show = course_to_show
#        break

    name = command[0]
    id_ = command[1]
    course = command[2]

#    name, id_, course = command.split(":")

    students.append({"name": name, "id": id_, "course": course})

for student in students:
    if course_to_show[0].startswith(student["course"][0:3]):
        print(f"{student['name']} - {student['id']}")
