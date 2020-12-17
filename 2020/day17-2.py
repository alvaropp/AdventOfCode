from copy import deepcopy
from itertools import product
import numpy as np
from numba import jit


neighbours = np.array(
    [
        neighbour
        for neighbour in product([-1, 0, 1], repeat=4)
        if neighbour != (0, 0, 0, 0)
    ]
)


@jit(nopython=True)
def update_node(space, i, j, k, l):
    dims = space.shape
    n_neighs = 0
    for delta in neighbours:
        neigh_coords = np.array([i, j, k, l]) + delta
        if (
            (0 <= neigh_coords[0] < dims[0])
            and (0 <= neigh_coords[1] < dims[1])
            and (0 <= neigh_coords[2] < dims[2])
            and (0 <= neigh_coords[3] < dims[3])
        ):
            n_neighs += space[
                neigh_coords[0], neigh_coords[1], neigh_coords[2], neigh_coords[3]
            ]

    node_state = space[i][j][k][l]

    if (node_state == 1 and n_neighs in [2, 3]) or (node_state == 0 and n_neighs == 3):
        return 1
    else:
        return 0


@jit
def solve(space, n_cycles):
    for _ in range(n_cycles):
        space = np.pad(space, 1)
        new_space = deepcopy(space)
        for i in range(new_space.shape[0]):
            for j in range(new_space.shape[1]):
                for k in range(new_space.shape[2]):
                    for l in range(new_space.shape[3]):
                        new_space[i, j, k, l] = update_node(space, i, j, k, l)
        space = new_space
    return space.sum()


with open("day17.txt", "r") as f:
    data = np.array([list(line) for line in f.read().splitlines()])

space = np.zeros(data.shape, dtype=int)
space[np.where(data == "#")] = 1

space = np.expand_dims(space, axis=(0, 1))

# Solve tiny case for JIT
_ = solve(space, 1)
# Main solution
print(solve(space, 6))
