import numpy as np


with open("day19.txt") as f:
    data = [x[:-1] for x in f.readlines()]

# Position
pos = 0
while data[0][pos] == " ":
    pos += 1
pos = np.array([0, pos])
previousPos = pos

# Direction
dirs = {'u': np.array([-1, 0]),
        'r': np.array([0, 1]),
        'd': np.array([1, 0]),
        'l': np.array([0, -1])}

markers = {'u': '|',
           'r': '-',
           'd': '|',
           'l': '-'}
oposite = {'u': 'd',
           'r': 'l',
           'd': 'u',
           'l': 'r'}
direction = "d"
collectedLetters = []


for i in range(100000):
    newDirection = None
    
    # Potentially collect letter
    if data[pos[0]][pos[1]] not in ['-', '|', '+', '']:
        collectedLetters.append(data[pos[0]][pos[1]])
    # Update pos
    newPos = pos + dirs[direction]
    if data[newPos[0]][newPos[1]] != " ":
        pos = newPos

    # Update dir
    if data[newPos[0]][newPos[1]] == "+":
        for key in dirs:
            if key != direction and key != oposite[direction]:
                newPos = pos + dirs[key]
                if data[newPos[0]][newPos[1]] != " ":
                    newDirection = key
                    break
    if newDirection != direction and newDirection is not None:
        direction = newDirection

    # Check for movement
    if any(newPos != pos) and newDirection is None:
        print("Result =", i+1)
        break
