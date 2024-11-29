import re

text = input()
pattern1 = r"([:|*]{2,})([A-Z][a-z]{2,})\1"
pattern2 = r"\d"

threshold = 1
cool_emojis = []

match_numbers = re.findall(pattern2, text)
for number in match_numbers:
    threshold *= int(number)
match_emojis = re.findall(pattern1, text)
for emoji in match_emojis:
    value = 0
    for char in emoji[1]:
        value += ord(char)
    if value >= threshold:
        cool_emoji = emoji[0] + emoji[1] + emoji[0]
        cool_emojis.append(cool_emoji)

print(f"Cool threshold: {threshold}")
print(f"{len(match_emojis)} emojis found in the text. The cool ones are:")
for index in range(len(cool_emojis)):
    print(f"{cool_emojis[index]}")
