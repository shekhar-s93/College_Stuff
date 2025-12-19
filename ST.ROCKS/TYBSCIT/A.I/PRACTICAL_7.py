import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
royals = ["J", "Q", "K", "A"]

cardfaces = [str(i) for i in range(2, 11)] + royals

deck = []
for suit in suits:
    for face in cardfaces:
        deck.append(face + " of " + suit)

random.shuffle(deck)

print("Name: Shekhar Suman")
print("Roll No: 47\n")

for card in deck:
    print(card)

import itertools, random

deck = list(itertools.product(
    ['2','3','4','5','6','7','8','9','10','J','Q','K','A'],
    ['Spade','Heart','Diamond','Club']
))

random.shuffle(deck)

print("\nYou got:")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])