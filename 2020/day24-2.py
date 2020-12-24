
with open("day24.txt", "r") as f:
    all_moves = f.read().splitlines()


moves = {
    "e": (1, -1, 0),
    "se": (1, 0, -1),
    "sw": (0, 1, -1),
    "w": (-1, 1, 0),
    "nw": (-1, 0, 1),
    "ne": (0, -1, 1),
}


def move_pos(pos, move):
    return (pos[0] + move[0], pos[1] + move[1], pos[2] + move[2])


def compute_neighbours(pos):
    return (
        sum(tuple(move_pos(pos, move)) in blacks for move in moves.values()),
        [move_pos(pos, move) for move in moves.values()],
    )


# Initial state

blacks = set()

for move in all_moves:
    start_pos = [0, 0, 0]
    i = 0
    while i < len(move):
        if move[i] in ["e", "w"]:
            start_pos = move_pos(start_pos, moves[move[i]])
            i += 1
        else:
            start_pos = move_pos(start_pos, moves[move[i : i + 2]])
            i += 2

    final_pos = tuple(start_pos)

    if tuple(final_pos) in blacks:
        blacks.remove(final_pos)
    else:
        blacks.add(final_pos)


# Iterate

n_iter = 100
for _ in range(n_iter):
    new_blacks = set()

    to_check = []
    for pos in blacks:
        n_neighs, neighbour_pos = compute_neighbours(pos)
        to_check.extend(neighbour_pos)
        if n_neighs != 0 and n_neighs <= 2:
            new_blacks.add(pos)

    for pos in to_check:
        n_neighs, neighbour_pos = compute_neighbours(pos)
        if n_neighs == 2:
            new_blacks.add(pos)

    blacks = new_blacks

print(len(blacks))
