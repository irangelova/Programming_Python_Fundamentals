company_users = {}

while True:
    entry = input()

    if entry == "End":
        break

    company_name = entry.split(" -> ")[0]
    employee_id = entry.split(" -> ")[1]

    if company_name not in company_users:
        company_users[company_name] = []
    if employee_id not in company_users[company_name]:
        company_users[company_name].append(employee_id)

for name in company_users.keys():
    print(f"{name}")
    for id_ in company_users[name]:
        print(f"-- {id_}")
