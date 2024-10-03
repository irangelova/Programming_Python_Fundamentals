players_A = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
players_B = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]

players = input().split()
game_terminated = False

for player in players:
    if player in players_A:
        players_A.remove(player)
    elif player in players_B:
        players_B.remove(player)

    if len(players_A) < 7 or len(players_B) < 7:
        game_terminated = True
        break

print(f"Team A - {len(players_A)}; Team B - {len(players_B)}")

if game_terminated:
    print("Game was terminated")