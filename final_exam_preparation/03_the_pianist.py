initial_pieces = int(input())

pieces = {}

for _ in range(initial_pieces):
    pieces_data = input().split('|')
    piece, composer, key = pieces_data[0], pieces_data[1], pieces_data[2]
    pieces[piece] = {"composer": composer, "key": key}

while True:
    command = input().split("|")
    if command[0] == "Stop":
        break
    elif command[0] == "Add":
        current_piece, current_composer, current_key = command[1], command[2], command[3]
        if current_piece not in pieces.keys():
            pieces[current_piece] = {"composer": current_composer, "key": current_key}
            print(f"{current_piece} by {current_composer} in {current_key} added to the collection!")
        else:
            print(f"{current_piece} is already in the collection!")
    elif command[0] == "Remove":
        current_piece = command[1]
        if current_piece in pieces.keys():
            pieces.pop(current_piece)
            print(f"Successfully removed {current_piece}!")
        else:
            print(f"Invalid operation! {current_piece} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        current_piece, new_key = command[1], command[2]
        if current_piece in pieces.keys():
            pieces[current_piece]["key"] = new_key
            print(f"Changed the key of {current_piece} to {new_key}!")
        else:
            print(f"Invalid operation! {current_piece} does not exist in the collection.")

for piece_, data in pieces.items():
    print(f"{piece_} -> Composer: {data['composer']}, Key: {data['key']}")
