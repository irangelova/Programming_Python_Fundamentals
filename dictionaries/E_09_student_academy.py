count_of_students = int(input())
grades_dictionary = {}
current_student = ""

for student in range(2 * count_of_students):
    information = input()

    if student % 2 == 0:
        current_student = information
        if current_student not in grades_dictionary:
            grades_dictionary[current_student] = []
    else:
        grades_dictionary[current_student].append(float(information))

for student in grades_dictionary.keys():
    average_grade = round(sum(grades_dictionary[student]) / len(grades_dictionary[student]), 2)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")
