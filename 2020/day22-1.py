from collections import deque

with open("day22.txt", "r") as f:
    data = f.read().splitlines()

decks = [deque([]), deque([])]

player = 0
for line in data[1:]:
    if line == "":
        continue
    if line == "Player 2:":
        player += 1
        continue
    decks[player].append(int(line))


deck_1, deck_2 = decks

while len(deck_1) and len(deck_2):
    card_1 = deck_1.popleft()
    card_2 = deck_2.popleft()

    if card_1 > card_2:
        deck_1.append(card_1)
        deck_1.append(card_2)
    elif card_1 < card_2:
        deck_2.append(card_2)
        deck_2.append(card_1)

winning_deck = deck_1 if not len(deck_2) else deck_2

points = 0
mult = 1
while winning_deck:
    points += mult * winning_deck.pop()
    mult += 1

print(points)

