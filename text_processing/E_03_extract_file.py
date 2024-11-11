entry = input().split(".")
file_extension = entry[1]
file_name = entry[0].split("\\")[-1]

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
