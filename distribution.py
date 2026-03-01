cards_per_player = len(deck) // num_players

for i in range (cards_per_player*num_players):
    player_index = i % num_players
    players[player_index]['hand'].append(deck[i])