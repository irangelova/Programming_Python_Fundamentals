fires_with_cells = input().split("#")
water = int(input())
total_effort = 0
total_fire = 0
cells_put_out = []

for fire in range(len(fires_with_cells)):
    current_fire = (fires_with_cells[fire]).split(" = ")
    fire_type = current_fire[0]
    cell_value = int(current_fire[1])

    if fire_type == "High":
        if 81 <= cell_value <= 125:
            if water < cell_value:
                break
            water -= cell_value
            total_effort += 0.25 * cell_value
            total_fire += cell_value
            cells_put_out.append(cell_value)
    elif fire_type == "Medium":
        if 50 <= cell_value <= 80:
            if water < cell_value:
                break
            water -= cell_value
            total_effort += 0.25 * cell_value
            total_fire += cell_value
            cells_put_out.append(cell_value)
    elif fire_type == "Low":
        if 1 <= cell_value <= 50:
            if water < cell_value:
                break
            water -= cell_value
            total_effort += 0.25 * cell_value
            total_fire += cell_value
            cells_put_out.append(cell_value)

print("Cells:")
for cell in cells_put_out:
    print(f"- {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")

