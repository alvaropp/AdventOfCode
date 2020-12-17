from copy import deepcopy
from itertools import product
import numpy as np


with open("day17.txt", "r") as f:
    data = np.array([list(line) for line in f.read().splitlines()])

space = np.zeros(data.shape, dtype=int)
space[np.where(data == "#")] = 1
space = np.expand_dims(space, axis=0)

neighbours = np.array(
    [neighbour for neighbour in product([-1, 0, 1], repeat=3) if neighbour != (0, 0, 0)]
)


def update_node(i, j, k):
    dims = space.shape
    neigh_values = []
    for delta in neighbours:
        neigh_coords = np.array([i, j, k]) + delta
        if all(0 <= coord < dims[i] for i, coord in enumerate(neigh_coords)):
            neigh_values.append(
                space[neigh_coords[0], neigh_coords[1], neigh_coords[2]]
            )

    node_state = space[i][j][k]
    n_neighs = sum(neigh_values)
    if (node_state == 1 and n_neighs in [2, 3]) or (node_state == 0 and n_neighs == 3):
        return 1
    else:
        return 0


n_cycles = 6

for n in range(n_cycles):
    space = np.pad(space, 1)
    new_space = deepcopy(space)
    for i in range(new_space.shape[0]):
        for j in range(new_space.shape[1]):
            for k in range(new_space.shape[2]):
                # print(i, j, k)
                new_space[i, j, k] = update_node(i, j, k)
    space = new_space

print(space.sum())
