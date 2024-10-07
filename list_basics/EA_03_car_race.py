step_times = input().split()
middle_of_steps_times = len(step_times) // 2
first_car = step_times[:middle_of_steps_times]
second_car = step_times[middle_of_steps_times + 1:]
total_time_first_car = total_time_second_car = 0

for time in first_car:
    total_time_first_car += int(time)
    if int(time) == 0:
        total_time_first_car *= 0.8

second_car.reverse()

for time in second_car:
    total_time_second_car += int(time)
    if int(time) == 0:
        total_time_second_car *= 0.8

if total_time_first_car < total_time_second_car:
    print(f"The winner is left with total time: {total_time_first_car:.1f}")
elif total_time_second_car < total_time_first_car:
    print(f"The winner is right with total time: {total_time_second_car:.1f}")
