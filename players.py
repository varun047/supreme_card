num_players = int(input("Enter the number of players(3-5): "))

if num_players < 3 or num_players > 5:
    print(f"Enter valid number if players, game not possible with {num_players} players")
    exit()

players =[]
for i in range(1, num_players+1):
        player = {
            "name": input(f"Enter name of player {i}: "),
            "hand": [],
            "score": 0
        }
        players.append(player)    

print("Players in the game:")
for p in players:
    print(p)
