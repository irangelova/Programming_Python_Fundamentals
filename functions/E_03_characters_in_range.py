def characters_in_range(start: str, finish: str, found_characters: list) -> list:
    for character in range(ord(start) + 1, ord(finish)):
        found_characters.append(chr(character))
    return found_characters


start_character = input()
end_character = input()
final_characters = []
characters_in_range(start_character, end_character, final_characters)
result = " ".join(final_characters)
print(result)
