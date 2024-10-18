elements = input().split()
moves = 0
all_elements_guessed = False
game_ended = False

while True:
    command = input().split()
    moves += 1

    if command[0] == "end":
        game_ended = True
        break

    first_index = int(command[0])
    second_index = int(command[1])

    if first_index == second_index or not 0 <= first_index <= len(elements) - 1 or not 0 <= second_index <= len(elements) - 1:
        middle_of_elements = len(elements) // 2
        elements.insert(middle_of_elements, f"-{moves}a")
        elements.insert(middle_of_elements, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
    elif elements[first_index] == elements[second_index]:
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")
        elements.pop(max(first_index, second_index))
        elements.pop(min(first_index, second_index))
    else:
        print("Try again!")

    if len(elements) == 0:
        all_elements_guessed = True
        break

if game_ended:
    print(f"Sorry you lose :(")
    print(" ".join(elements))

if all_elements_guessed:
    print(f"You have won in {moves} turns!")
