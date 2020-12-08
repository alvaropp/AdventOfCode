from collections import defaultdict
from copy import deepcopy

with open("day8.txt", "r") as f:
    code = [instruction.split(" ") for instruction in f.read().splitlines()]


def run_program(code):
    visited = defaultdict(int)
    pos = 0
    acc = 0
    n_lines = len(code)

    running = True
    while running:
        if pos == n_lines:
            running = False
            break

        visited[pos] += 1
        if visited[pos] > 1:
            break

        instruction, value = code[pos]

        if instruction == "acc":
            acc += int(value)
            pos += 1
        elif instruction == "jmp":
            pos += int(value)
        elif instruction == "nop":
            pos += 1
        else:
            raise ValueError(f"Unknown instruction: {instruction}.")

    return (not running, acc)


swap = {"nop": "jmp", "jmp": "nop"}
idx_to_change = [idx for idx in range(len(code)) if code[idx][0] in ["jmp", "nop"]]

for idx in idx_to_change:
    new_code = deepcopy(code)
    new_code[idx][0] = swap[new_code[idx][0]]

    finished, acc = run_program(new_code)
    if finished:
        print(acc)
        break
