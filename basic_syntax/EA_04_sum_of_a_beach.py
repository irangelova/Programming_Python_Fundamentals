input_string = input()
words_to_count = ["sand", "water", "fish", "sun"]
input_string_lower = input_string.lower()

word_count = {word: input_string_lower.count(word) for word in words_to_count}

total_count = sum(word_count.values())

print(total_count)