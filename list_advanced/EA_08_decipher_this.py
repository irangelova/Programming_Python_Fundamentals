initial_message = input().split()
count_words = len(initial_message)
deciphered_message = []

for word in range(0, count_words):
    char_code = []
    current_word = list(initial_message[word])
    for position in range(len(current_word) - 1, -1, -1):
        if current_word[position].isdigit():
            char_code.insert(0, current_word[position])
            current_word.remove(current_word[position])
    char_code_cleaned = "".join(char_code)
    new_first_letter = chr(int(char_code_cleaned))
    current_word.insert(0, new_first_letter)
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    deciphered_message.append("".join(current_word))

print(" ".join(deciphered_message))

