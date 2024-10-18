int_sequence = list(map(int, input().split()))

average = sum(int_sequence) / len(int_sequence)
list_with_top_5 = []

for element in int_sequence:
    if element > average:
        list_with_top_5.append(element)

list_with_top_5.sort(reverse=True)
while len(list_with_top_5) > 5:
    list_with_top_5.pop()

if len(list_with_top_5) == 0:
    print("No")
else:
    print(" ".join(map(str, list_with_top_5)))

