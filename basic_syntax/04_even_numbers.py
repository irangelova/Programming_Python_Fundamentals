number = int(input())

for num in range(1, number + 1):
    digit = int(input())
    if digit % 2 != 0:
        print(f"{digit} is odd!")
        break
else:
    print("All numbers are even.")