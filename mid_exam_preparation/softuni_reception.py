from math import ceil

first_employee_capacity = int(input())
second_employee_capacity = int(input())
third_employee_capacity = int(input())
students_count = int(input())
number_of_breaks = 0

total_capacity = first_employee_capacity + second_employee_capacity + third_employee_capacity
total_hours_without_break = students_count / total_capacity
hours_for_break = total_hours_without_break

while hours_for_break / 4 >= 1:
    number_of_breaks += 1
    hours_for_break -= 3

total_hours_with_break = total_hours_without_break + number_of_breaks
print(f"Time needed: {ceil(total_hours_with_break)}h.")
