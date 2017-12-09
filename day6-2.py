import numpy as np


def updateState(state):
    pos = np.argmax(state)
    blocks = state[pos]
    state[pos] = 0
    for b in range(blocks):
        state[(pos+b+1) % len(state)] += 1


# Load input
with open("day6.txt") as f:
    state = [int(x) for x in f.readline().strip().split()]

# Remember states
stateHistory = []

# Loop over until repetition
while state not in stateHistory:
    stateHistory.append(state.copy())
    updateState(state)

print("Solution = ", len(stateHistory) - stateHistory.index())
