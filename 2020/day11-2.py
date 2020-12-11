from copy import deepcopy


def update_node(row, col):

    node = floor[row][col]

    mask = []
    for (row_move, col_move) in directions:
        look_node = "."
        look_row = row + row_move
        look_col = col + col_move
        while (0 <= look_row < n_rows) and (0 <= look_col < n_cols):
            look_node = floor[look_row][look_col]
            if look_node in "#L":
                break
            look_row += row_move
            look_col += col_move
        mask.append(look_node)

    if node == "L" and mask.count("#") == 0:
        return "#"
    elif node == "#" and mask.count("#") >= 5:
        return "L"
    else:
        return node


with open("day11.txt", "r") as f:
    floor = [list(line) for line in f.read().splitlines()]

n_rows = len(floor)
n_cols = len(floor[0])

directions = [
    [1, 0],
    [1, 1],
    [0, 1],
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [1, -1],
]


while True:
    new_floor = deepcopy(floor)

    for row in range(n_rows):
        for col in range(n_cols):
            new_floor[row][col] = update_node(row, col)
    if floor != new_floor:
        floor = deepcopy(new_floor)
    else:
        break

print(sum(line.count("#") for line in new_floor))
