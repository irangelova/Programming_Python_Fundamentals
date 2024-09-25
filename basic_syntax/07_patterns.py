max_number_stars = int(input())

for star1 in range(1, max_number_stars + 1):
    for star2 in range(0, star1):
        print("*", end="")
    print()
for star1 in range(max_number_stars - 1, 0, -1):
    for star2 in range(0, star1):
        print("*", end="")
    print()
