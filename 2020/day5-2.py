import numpy as np

with open("day5.txt", "r") as f:
    boarding_passes = f.read().splitlines()

n_rows = 128
n_columns = 8


def apply_partition(current_range, instructions):
    for instruction in instructions:
        if instruction in ["F", "L"]:
            current_range = [
                current_range[0],
                current_range[1] - 1 - (current_range[1] - current_range[0]) // 2,
            ]
        elif instruction in ["B", "R"]:
            current_range = [
                current_range[1] - 1 - (current_range[1] - current_range[0]) // 2 + 1,
                current_range[1],
            ]
        else:
            raise ValueError("Unknown instruction.")
    assert current_range[0] == current_range[1]
    return current_range[0]


def compute_seat(boarding_pass):
    row_range = [0, n_rows - 1]
    row = apply_partition(row_range, boarding_pass[:-3])
    column_range = [0, n_columns - 1]
    column = apply_partition(column_range, boarding_pass[-3:])
    return row * 8 + column


occupied_seats = np.array(
    sorted([compute_seat(boarding_pass) for boarding_pass in boarding_passes])
)
missing_idx = np.where([np.diff(occupied_seats) == 2])[-1][0]


print(occupied_seats[missing_idx + 1] - 1)
