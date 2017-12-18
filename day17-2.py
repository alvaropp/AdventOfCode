from numba import jit


@jit
def solve(step, maxNum):
    pos = 0
    solution = 0
    for num in range(1, int(maxNum)+1):
        pos = (pos + step)%num + 1
        if pos == 1:
            solution = num
    return solution

step = 371
maxNum = 50000000
print("Result =", solve(step, maxNum))
