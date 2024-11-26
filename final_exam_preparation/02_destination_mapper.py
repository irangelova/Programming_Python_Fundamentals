import re

destinations = input()
pattern = r"(=|\/)([A-Z][A-Za-z]{3,})\1"
matches = re.findall(pattern, destinations)
travel_points = 0

for destination in matches:
    travel_points += len(destination[1])
valid_destinations = [destination[1] for destination in matches]

print(f"Destinations: {', '.join(valid_destinations)}")
print(f"Travel Points: {travel_points}")
