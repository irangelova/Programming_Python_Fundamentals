text = input()


def replace_strings(string: str, old_string: str, new_string: str) -> str:
    string = string.replace(old_string, new_string)
    return string


def is_included(string: str, string_to_search: str) -> str:
    if string_to_search in string:
        return "True"
    return "False"


def ends_with(string: str, string_to_check: str) -> str:
    if string.endswith(string_to_check):
        return "True"
    else:
        return "False"


def uppercase(string: str) -> str:
    string = string.upper()
    return string


def find_index(string: str, char_to_find: str) -> int:
    position = text.index(char_to_find)
    return position


def cut(string: str, start: int, count: int) -> str:
    cut_string = string[start:(start + count)]
    return cut_string


while True:
    command = input().split()
    if command[0] == "Done":
        break
    elif command[0] == "Change":
        char = command[1]
        replacement = command[2]
        text = replace_strings(text, char, replacement)
        print(text)
    elif command[0] == "Includes":
        substring = command[1]
        result = is_included(text, substring)
        print(result)
    elif command[0] == "End":
        substring = command[1]
        result = ends_with(text, substring)
        print(result)
    elif command[0] == "Uppercase":
        text = uppercase(text)
        print(text)
    elif command[0] == "FindIndex":
        char = command[1]
        result = find_index(text, char)
        print(result)
    elif command[0] == "Cut":
        start_index = int(command[1])
        count_cut = int(command[2])
        cut_chars = cut(text, start_index, count_cut)
        print(cut_chars)
