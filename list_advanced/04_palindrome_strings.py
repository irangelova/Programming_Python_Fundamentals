input_words = input().split()
searched_palindrome = input()
palindromes = []

for word in input_words:
    if word == "".join(reversed(word)):
        palindromes.append(word)

print(palindromes)
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")
