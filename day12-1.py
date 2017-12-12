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

# Find all connections from a given program
program = 0
connections = []
queue = [x for x in np.where(pipes[program] != 0)[0]]

while queue:
    element = queue.pop(0)
    if element not in connections:
        connections.extend([element])
    queue.extend([x for x in np.where(pipes[element] != 0)[0] if (x is not program) and not x in connections])

print("Result=", len(connections))
