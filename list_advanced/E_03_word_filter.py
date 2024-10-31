input_text = input().split()
text_to_print = [word for word in input_text if len(word) % 2 == 0]

print("\n".join(text_to_print))
