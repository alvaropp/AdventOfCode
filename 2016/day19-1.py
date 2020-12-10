import numpy as np
from numba import jit

with open("day19.txt", "r") as f:
    n_elves = int(f.read().strip())


@jit(nopython=True)
def solve(n_elves):
    presents = [1] * n_elves
    elf = 0

    for _ in range(n_elves - 1):

        jump_1 = 1
        while presents[(elf + jump_1) % n_elves] == 0:
            jump_1 += 1

        presents[(elf + jump_1) % n_elves] = 0

        jump_2 = 1
        while presents[(elf + jump_1 + jump_2) % n_elves] == 0:
            jump_2 += 1

        elf = (elf + jump_1 + jump_2) % n_elves

    return presents


# Just in time compilation with a short one
_ = np.where(np.array(solve(5)) != 0)[0][0] + 1

print(np.where(np.array(solve(n_elves)) != 0)[0][0] + 1)
