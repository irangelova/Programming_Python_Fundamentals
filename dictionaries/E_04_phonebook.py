phonebook = {}

while True:
    entries = input()

    if entries.isdigit():
        break

    contact_name = entries.split("-")[0]
    contact_number = entries.split("-")[1]

    if contact_name not in phonebook.keys():
        phonebook[contact_name] = 0
    phonebook[contact_name] = contact_number

for entry in range(int(entries)):
    searched_contact_name = input()
    if searched_contact_name in phonebook.keys():
        print(f"{searched_contact_name} -> {phonebook[searched_contact_name]}")
    else:
        print(f"Contact {searched_contact_name} does not exist.")
