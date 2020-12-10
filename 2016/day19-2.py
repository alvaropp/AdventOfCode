import numpy as np
from numba import jit

with open("day19.txt", "r") as f:
    n_elves = int(f.read().strip())


@jit(nopython=True)
def solve(n_elves):
    presents = [1] * n_elves
    elf = 0

    n_remaining = n_elves

    for _ in range(n_elves - 1):

        active_passed = 0
        jump_1 = 0
        while active_passed < n_remaining // 2:
            jump_1 += 1
            if presents[(elf + jump_1) % n_elves] == 1:
                active_passed += 1
            if jump_1 > n_elves:
                print("warning jump_1")
                return None

        presents[(elf + jump_1) % n_elves] = 0

        jump_2 = 1
        while presents[(elf + jump_2) % n_elves] == 0:
            if jump_2 > n_elves:
                print("warning jump_2")
                return None
            jump_2 += 1

        elf = (elf + jump_2) % n_elves
        n_remaining -= 1

    return presents


# Just in time compilation with a short one
_ = np.where(np.array(solve(5)) == 1)[0][0] + 1

print(np.where(np.array(solve(n_elves)) == 1)[0][0] + 1)
