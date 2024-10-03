cards_strings = input().split()
count_shuffles = int(input())

for shuffle in range(count_shuffles):
    first_half_deck = cards_strings[:int(len(cards_strings) // 2)]
    second_half_deck = cards_strings[int(len(cards_strings) // 2):]

    shuffled_deck = []

    for card_index in range(len(first_half_deck)):
        shuffled_deck.append(first_half_deck[card_index])
        shuffled_deck.append(second_half_deck[card_index])
    cards_strings = shuffled_deck

print(shuffled_deck)