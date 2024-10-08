import random
from colorama import Fore

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = ""
player_wins = computer_wins = draw_rounds = 0

while True:
    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
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
        print(Fore.GREEN + "You win!")
    elif player_move == computer_move:
        draw_rounds += 1
        print(Fore.YELLOW + "Draw!")
    else:
        computer_wins += 1
        print(Fore.RED + "You lose!")

    ask_for_new_game = input(Fore.WHITE + "Do you want to start another game? Type [yes] or [no]? ")
    if ask_for_new_game == "yes":
        continue
    elif ask_for_new_game == "no":
        break
    else:
        raise SystemExit("Invalid Input. Try again...")

print(f"You won {player_wins} rounds.")
print(f"Computer won {computer_wins} rounds.")
print(f"Total {draw_rounds} rounds were draw.")
