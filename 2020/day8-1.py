from collections import defaultdict


with open("day8.txt", "r") as f:
    code = [instruction.split(" ") for instruction in f.read().splitlines()]

visited = defaultdict(int)
pos = 0
acc = 0
while True:
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

print(acc)
