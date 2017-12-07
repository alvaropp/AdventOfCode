import time
from numba import jit


@jit
def solve(maze):
    pos = 0
    jumps = 0
    while pos >= 0 and pos < len(maze):
        if maze[pos] >= 3:
            maze[pos] -= 1
            pos = pos + maze[pos] + 1
        else:
            maze[pos] += 1
            pos = pos + maze[pos] - 1
        jumps += 1
    return jumps


with open("day5.txt") as f:
    maze = f.readlines()
    maze = [int(x.strip()) for x in maze]

jumps = solve(maze)

print("Solution = ", jumps)
