count_triples = int(input())

for letter1 in range(97, 97 + count_triples):
    for letter2 in range(97, 97 + count_triples):
        for letter3 in range(97, 97 + count_triples):
            print(f"{chr(letter1)}{chr(letter2)}{chr(letter3)}")

