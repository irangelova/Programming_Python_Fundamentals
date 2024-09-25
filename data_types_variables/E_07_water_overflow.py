tank_capacity = 255
number_pours = int(input())

for pour in range(number_pours):
    litres_to_pour = int(input())
    if tank_capacity - litres_to_pour < 0:
        print("Insufficient capacity!")
        continue
    tank_capacity -= litres_to_pour

print(255 - tank_capacity)