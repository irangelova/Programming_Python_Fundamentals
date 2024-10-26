from math import floor

number_of_biscuits_daily = int(input())
count_of_workers = int(input())
number_of_biscuits_competitor = int(input())
total_produced_biscuits = 0


for day in range(1, 31):
    if day % 3 == 0:
        total_produced_biscuits += floor(0.75 * number_of_biscuits_daily * count_of_workers)
    else:
        total_produced_biscuits += floor(number_of_biscuits_daily * count_of_workers)

print(f"You have produced {total_produced_biscuits} biscuits for the past month.")
difference = abs(total_produced_biscuits - number_of_biscuits_competitor)
percentage = (difference / number_of_biscuits_competitor) * 100

if total_produced_biscuits > number_of_biscuits_competitor:
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    print(f"You produce {percentage:.2f} percent less biscuits.")



