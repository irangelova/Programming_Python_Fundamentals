time_in_centuries = int(input())

time_in_years = time_in_centuries * 100
time_in_days = int(time_in_years * 365.2422)
time_in_hours = time_in_days * 24
time_in_minutes = time_in_hours * 60

print(f"{time_in_centuries} centuries = {time_in_years} years = {int(time_in_days)} days = {int(time_in_hours)} hours = {int(time_in_minutes)} minutes")

