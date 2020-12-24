import numpy as np


with open("day24.txt", "r") as f:
    all_moves = f.read().splitlines()

moves = {
    "e": np.array([1, -1, 0]),
    "se": np.array([1, 0, -1]),
    "sw": np.array([0, 1, -1]),
    "w": np.array([-1, 1, 0]),
    "nw": np.array([-1, 0, 1]),
    "ne": np.array([0, -1, 1]),
}
black = set()

for move in all_moves:
    start_pos = np.zeros(3)
    i = 0
    while i < len(move):
        if move[i] in ["e", "w"]:
            start_pos += moves[move[i]]
            i += 1
        else:
            start_pos += moves[move[i : i + 2]]
            i += 2
    final_pos = tuple(start_pos)

    if tuple(final_pos) in black:
        black.remove(final_pos)
    else:
        black.add(final_pos)

print(len(black))
