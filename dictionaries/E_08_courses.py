courses_student_count = {}
courses_student_names = {}

while True:
    entry = input()
    if entry == "end":
        break

    course_name = entry.split(" : ")[0]
    student_name = entry.split(" : ")[1]

    counter_students = 0
    if course_name not in courses_student_count.keys():
        courses_student_count[course_name] = 0
        courses_student_names[course_name] = []
    courses_student_count[course_name] += 1
    courses_student_names[course_name].append(student_name)

for course, count in courses_student_count.items():
    print(f"{course}: {count}")
    student_names = courses_student_names[course]
    for student in student_names:
        print(f"-- {student}")
