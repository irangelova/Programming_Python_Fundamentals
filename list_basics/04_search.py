count_words = int(input())
special_word = input()
original_input = []
filtered_input = []

for word in range(count_words):
    current_string = input()
    original_input.append(current_string)
print(original_input)

for input_string in range(len(original_input)):
    string_to_check = original_input[input_string]
    if special_word in string_to_check:
        filtered_input.append(string_to_check)

print(filtered_input)
