import re

bought_furniture = []
total_cost = 0

while True:
    command = input()

    if command == "Purchase":
        break

    pattern = r">>(\w+)<<(\d+\.?\d+)!(\d+)"
    match = re.search(pattern, command)
    if match:
        bought_furniture.append(match.group(1))
        total_cost += float(match.group(2)) * int(match.group(3))

print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")
