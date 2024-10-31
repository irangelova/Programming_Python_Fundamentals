current_version = input().split(".")
current_version_as_integer = int("".join(current_version))
next_version = current_version_as_integer + 1
next_version_as_list = [string for string in str(next_version)]
print(".".join(next_version_as_list))
