starting_list = input().split()
number_commands = int(input())

for number_command in range(1, number_commands + 1):
    command = input().split(" * ")
    action = command[0]

    if action == "Add Song":
        song_to_add = command[1]
        if song_to_add not in starting_list:
            starting_list.append(song_to_add)
            print(f"{song_to_add} successfully added")
        else:
            starting_list = starting_list
    elif action == "Delete Song":
        list_of_deleted_songs = []
        count_of_songs_to_delete = int(command[1])
        if len(starting_list) >= count_of_songs_to_delete:
            for count in range(count_of_songs_to_delete):
                list_of_deleted_songs.append(starting_list[0])
                starting_list.pop(0)
            print(f"{','.join(list_of_deleted_songs)} deleted")
        else:
            starting_list = starting_list
    elif action == "Shuffle Songs":
        first_index = int(command[1])
        second_index = int(command[2])
        if 0 <= first_index <= (len(starting_list) - 1) and 0 <= second_index <= (len(starting_list) - 1):
            starting_list[first_index], starting_list[second_index] = starting_list[second_index], starting_list[first_index]
            print(f"{starting_list[first_index]} is swapped with {starting_list[second_index]}")
        else:
            starting_list = starting_list
    elif action == "Insert":
        song_to_insert = command[1]
        song_index = int(command[2])
        if 0 <= song_index <= (len(starting_list) - 1) and song_to_insert not in starting_list:
            starting_list.insert(song_index, song_to_insert)
            print(f"{song_to_insert} successfully inserted")
        elif 0 <= song_index <= (len(starting_list) - 1) and song_to_insert in starting_list:
            print("Song is already in the playlist")
        else:
            print("Index out of range")
    elif action == "Sort":
        starting_list.sort(reverse=True)
    elif action == "Play":
        print(f"Songs to Play:")
        print(*starting_list, sep='\n')
