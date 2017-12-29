import numpy as np


in_ = []
out_ = []

with open("day21.txt") as f:
    data = f.readlines()

for line in data:
    line = line.strip()
    line = [x.split('/') for x in line.split(" => ")]
    in_.append(np.array([list(x) for x in line[0]]))
    out_.append(np.array([list(x) for x in line[1]]))

# Split shapes 2 and 3
in_2 = in_[:6]
in_3 = in_[6:]
out_2 = out_[:6]
out_3 = out_[6:]


# Evolve pattern
def findPattern(miniSquare):
    if len(miniSquare) == 2:
        array = in_2
        arrayOut = out_2
    if len(miniSquare) == 3:
        array = in_3
        arrayOut = out_3
    # Rotation
    for r in range(4):
        test = np.rot90(miniSquare, r)
        try:
            ind = next((i for i, val in enumerate(array) if np.all(val==test)))
            break
        except:
            pass
        # Flip left-right
        try:
            test = np.fliplr(test)
            ind = next((i for i, val in enumerate(array) if np.all(val==test)))
        except:
            pass
        # Flip up-down
        try:
            test = np.flipud(test)
            ind = next((i for i, val in enumerate(array) if np.all(val==test)))
        except:
            pass
        # Transpose
        try:
            test = np.transpose(test)
            ind = next((i for i, val in enumerate(array) if np.all(val==test)))
        except:
            pass
    return arrayOut[ind]


pattern = np.array([['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']])

for i in range(18):
    print("Iteration", i)
    if len(pattern) % 3 == 0:
        nSquares = int(len(pattern) / 3)
        outputPattern = np.zeros([4*nSquares, 4*nSquares], dtype='<U1')
        for i in range(nSquares):
            for j in range(nSquares):
                miniSquare = pattern[3*i:3*(i+1), 3*j:3*(j+1)]
                miniOut = findPattern(miniSquare)
                outputPattern[4*i:4*(i+1), 4*j:4*(j+1)] = miniOut

    if len(pattern) % 2 == 0:
        nSquares = int(len(pattern) / 2)
        outputPattern = np.zeros([3*nSquares, 3*nSquares], dtype='<U1')
        for i in range(nSquares):
            for j in range(nSquares):
                miniSquare = pattern[2*i:2*(i+1), 2*j:2*(j+1)]
                miniOut = findPattern(miniSquare)
                outputPattern[3*i:3*(i+1), 3*j:3*(j+1)] = miniOut
    pattern = outputPattern.copy()

print("Result =", np.sum(pattern == "#"))

