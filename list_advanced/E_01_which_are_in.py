first_input = input().split(", ")
second_input = input().split(", ")
sorted_input = []

for word1 in first_input:
    for word2 in second_input:
        if word1 in word2:
            sorted_input.append(word1)
            break

print(sorted_input)