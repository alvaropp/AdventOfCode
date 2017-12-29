import numpy as np


# Load data
programs = []

filename = "day12.txt"
with open(filename) as f:
    # Find the number of programs
    N = len(f.readlines())
    # Build adjacency matrix
    pipes = np.zeros([N, N])

with open(filename) as f:
    # Populate the adjacency matrix
    for line in f.readlines():
        line = line.strip().split(" <-> ")
        origin = int(line[0])
        dests = [int(x.strip()) for x in line[1].strip().split(',')]
        for dest in dests:
            pipes[origin][dest] = 1

visitedPrograms = []
program = 0

while len([x for sublist in visitedPrograms for x in sublist]) < N:
    connections = []
    queue = [x for x in np.where(pipes[program] != 0)[0]]

    while queue:
        element = queue.pop(0)
        if element not in connections:
            connections.extend([element])
        queue.extend([x for x in np.where(pipes[element] != 0)[0] if (x is not program) and not x in connections])
    visitedPrograms.append(connections)

    if len([x for sublist in visitedPrograms for x in sublist]) == N:
        break
    # Choose another program which hasn't been visited already
    program = [x for x in list(range(N)) if not x in [x for sublist in visitedPrograms for x in sublist]][0]

print("Solution =", len(visitedPrograms))
