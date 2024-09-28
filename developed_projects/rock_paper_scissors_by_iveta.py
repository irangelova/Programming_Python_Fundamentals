import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = ""
player_wins = computer_wins = draw_rounds = 0

while True:
    player_move = input("Choose [r]ock, [p]aper, [s]cissors or [e]nd: ")
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    elif player_move == "e":
        break
    else:
        raise SystemExit("Invalid Input. Try again...")

    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors

    print(f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) \
            or (player_move == paper and computer_move == rock) \
            or (player_move == scissors and computer_move == paper):
        player_wins += 1
        print("You win!")
    elif player_move == computer_move:
        draw_rounds += 1
        print("Draw!")
    else:
        computer_wins += 1
        print("You lose!")

print(f"You won {player_wins} rounds.")
print(f"Computer won {computer_wins} rounds.")
print(f"Total {draw_rounds} rounds were draw.")
