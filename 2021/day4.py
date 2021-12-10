import re
from copy import deepcopy

import numpy as np
from numpy.core.arrayprint import _array_repr_implementation


def load_problem():
    with open("day4.txt", "r") as f:
        data = f.readlines()

    random_numbers = [int(number) for number in data[0].split(",")]

    boards = []
    board = np.zeros([5, 5], dtype=int)
    j = 0
    for i in range(2, len(data)):
        if data[i] == "\n":
            continue

        row = np.array([int(number) for number in re.findall("(\\d+)", data[i])])
        board[j, :] = row
        j += 1
        if j == 5:
            j = 0
            boards.append(deepcopy(board))
            board = np.zeros([5, 5], dtype=int)
    return random_numbers, boards


def is_bingo(board):
    return (-5 in board.sum(axis=0)) or (-5 in board.sum(axis=1))


def cross_number(board, number):
    board[board == number] = -1


def find_unmarked_numbers_board(board):
    return board[board != -1].sum()


random_numbers, boards = load_problem()

for random_number in random_numbers:
    for board in boards:
        cross_number(board, random_number)
    if any(is_bingo(board) for board in boards):
        winning_board = boards[np.where([is_bingo(board) for board in boards])[0][0]]
        break

print(f"Part 1: {find_unmarked_numbers_board(winning_board) * random_number}")


random_numbers, boards = load_problem()

winning_boards = set()
last_won_board = None
for random_number in random_numbers:
    for idx, board in enumerate(boards):
        if idx not in winning_boards:
            cross_number(board, random_number)

    already_won_boards = list(np.where([is_bingo(board) for board in boards])[0])
    if already_won_boards:
        last_won_board = [
            number for number in already_won_boards if number not in winning_boards
        ]
        winning_boards.update(already_won_boards)

    if len(winning_boards) == len(boards):
        break

print(
    f"Part 2: {find_unmarked_numbers_board(boards[last_won_board[0]]) * random_number}"
)
