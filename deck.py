import random

suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck = []

for suit in suits:
    for rank in ranks:
        card = (suit,rank)
        deck.append(card)

random.shuffle(deck)
print("Shuffled Deck:", deck)

