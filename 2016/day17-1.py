import hashlib
from collections import deque

with open("day17.txt", "r") as f:
    maze = f.read().splitlines()

vault_column, vault_row = 7, 7
hash_moves = ["U", "D", "L", "R"]
move_row_dict = {"U": -1, "D": 1, "L": 0, "R": 0}
move_column_dict = {"U": 0, "D": 0, "L": -1, "R": 1}


def compute_pos_from_path(path):
    row = sum(move_row_dict[move] * 2 for move in path)
    column = sum(move_column_dict[move] * 2 for move in path)
    return row + 1, column + 1


def get_available_moves(path, row, column):
    hash = hashlib.md5(path.encode("utf-8")).hexdigest()[:4]
    open_doors = [move for idx, move in enumerate(hash_moves) if hash[idx] in "bcdef"]
    physical_doors = [
        move
        for move in "UDLR"
        if maze[row + move_row_dict[move]][column + move_column_dict[move]] in "|-"
    ]
    return set(physical_doors) & set(open_doors)


def find_shortest_path(passcode):
    """Using BFS and rejecting candidate paths that are longer that the shortest
    path found to vault already."""
    all_paths_to_vault = []
    min_found_path = float("inf")

    paths_to_check = deque([""])
    while paths_to_check:
        path = paths_to_check.popleft()
        row, column = compute_pos_from_path(path)
        if row >= vault_row and column >= vault_column:
            all_paths_to_vault.append(path)
            min_found_path = len(path)
        if len(path) < min_found_path:
            potential_moves = get_available_moves(passcode + path, row, column)
            paths_to_check.extend(path + move for move in potential_moves)
    return min(all_paths_to_vault, key=len)


find_shortest_path("pgflpeqp")
