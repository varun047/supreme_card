import random

suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck = []

for suit in suits:
    for rank in ranks:
        card = (suit,rank)
        deck.append(card)

random.shuffle(deck)
# print("Shuffled Deck:", deck)


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



cards_per_player = len(deck) // num_players

for i in range (cards_per_player*num_players):
    player_index = i % num_players
    players[player_index]['hand'].append(deck[i])


for p in players:
    print(f"{p['name']}'s hand: {p['hand']}\n")


remainder_cards = deck[cards_per_player * num_players:]

if remainder_cards:
    print("Leftover cards:", remainder_cards)



