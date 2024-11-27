import re
mirror_words = []

text = input()
pattern = r"(#|@)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})\1"
matched_pairs = re.findall(pattern, text)

if not matched_pairs:
    print("No word pairs found!")
else:
    valid_pairs_count = len(matched_pairs)
    print(f"{valid_pairs_count} word pairs found!")
for pair in matched_pairs:
    if pair[1] == pair[3][::-1]:
        mirror_words.append(f"{pair[1]} <=> {pair[3]}")
if not mirror_words:
    print( "No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirror_words))
