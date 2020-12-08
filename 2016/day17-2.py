import hashlib

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


def find_longest_path(passcode):
    """Using BFS and finding all possible paths."""
    all_paths_to_vault = []

    paths_to_check = [""]
    while paths_to_check:
        path = paths_to_check.pop()
        row, column = compute_pos_from_path(path)
        if row >= vault_row and column >= vault_column:
            all_paths_to_vault.append(path)
        else:
            potential_moves = get_available_moves(passcode + path, row, column)
            paths_to_check.extend(path + move for move in potential_moves)
    return len(max(all_paths_to_vault, key=len))


find_longest_path("pgflpeqp")
