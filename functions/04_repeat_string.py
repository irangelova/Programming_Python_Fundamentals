repeat_string = lambda text, counter: counter * text

input_text = input()
current_counter = int(input())
result = repeat_string(input_text, current_counter)
print(result)