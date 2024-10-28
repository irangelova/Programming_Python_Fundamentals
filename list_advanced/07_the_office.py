employee_happiness = list(map(int, input().split()))
improvement_factor = int(input())
count_happy_employees = 0

employee_happiness = [happiness * improvement_factor for happiness in employee_happiness]
average_happiness = sum(employee_happiness) / len(employee_happiness)

for value in employee_happiness:
    if value >= average_happiness:
        count_happy_employees += 1

if count_happy_employees >= len(employee_happiness) / 2:
    print(f"Score: {count_happy_employees}/{len(employee_happiness)}. Employees are happy!")
else:
    print(f"Score: {count_happy_employees}/{len(employee_happiness)}. Employees are not happy!")

