##
## Run with pypy
##

import math
import time


def solve():
    length = int(1e5)
    tape = [0] * length
    nSteps = int(12861455)
    state = "A"
    pos = int(math.floor(length/2))

    for t in range(nSteps):
        if state == "A":
            if tape[pos] == 0:
                tape[pos] = 1
                pos += 1
                state = "B"
            else:
                tape[pos] = 0
                pos -= 1
                state = "B"
            continue

        if state == "B":
            if tape[pos] == 0:
                tape[pos] = 1
                pos -= 1
                state = "C"
            else:
                tape[pos] = 0
                pos += 1
                state = "E"
            continue

        if state == "C":
            if tape[pos] == 0:
                tape[pos] = 1
                pos += 1
                state = "E"
            else:
                tape[pos] = 0
                pos -= 1
                state = "D"
            continue

        if state == "D":
            if tape[pos] == 0:
                tape[pos] = 1
                pos -= 1
                state = "A"
            else:
                tape[pos] = 1
                pos -= 1
                state = "A"
            continue

        if state == "E":
            if tape[pos] == 0:
                tape[pos] = 0
                pos += 1
                state = "A"
            else:
                tape[pos] = 0
                pos += 1
                state = "F"
            continue

        if state == "F":
            if tape[pos] == 0:
                tape[pos] = 1
                pos += 1
                state = "E"
            else:
                tape[pos] = 1
                pos += 1
                state = "A"
            continue
    # Checksum
    print "Result =", int(sum(tape))

solve()

