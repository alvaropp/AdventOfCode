# Switched from deque to list as converting back and forth for deque slicing was slow


def solve_game(deck_1, deck_2):
    history = []

    while len(deck_1) and len(deck_2):

        if (deck_1, deck_2) in history:
            return 1, deck_1, deck_2

        history.append((deck_1[:], deck_2[:]))

        card_1 = deck_1.pop(0)
        card_2 = deck_2.pop(0)

        if (len(deck_1) >= card_1) and (len(deck_2) >= card_2):
            winner, _, _ = solve_game(deck_1[:card_1], deck_2[:card_2])
        else:
            winner = 1 if card_1 > card_2 else 2

        if winner == 1:
            deck_1.append(card_1)
            deck_1.append(card_2)
        else:
            deck_2.append(card_2)
            deck_2.append(card_1)

    winner = 1 if not len(deck_2) else 2
    return winner, deck_1, deck_2


def compute_points(deck):
    points = 0
    mult = 1
    while deck:
        points += mult * deck.pop()
        mult += 1
    return points


with open("day22.txt", "r") as f:
    data = f.read().splitlines()

decks = [[], []]

player = 0
for line in data[1:]:
    if line == "":
        continue
    if line == "Player 2:":
        player += 1
        continue
    decks[player].append(int(line))

deck_1, deck_2 = decks

winner, deck_1, deck_2 = solve_game(deck_1, deck_2)
print(compute_points(deck_1)) if winner == 1 else print(compute_points(deck_2))
