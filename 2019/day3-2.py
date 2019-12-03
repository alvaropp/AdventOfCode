import numpy as np

with open("day3.txt") as f:
    data = [line.strip().split(",") for line in f.readlines()]


delta_pos = {"U": [+1, 0], "D": [-1, 0], "R": [0, +1], "L": [0, -1]}

pos = np.zeros(2)
pos_list_1 = [list(pos)]
cable = 0
for instruction in data[cable]:
    direction = instruction[0]
    length = int(instruction[1:])
    for l in range(length):
        pos += np.array(delta_pos[direction])
        pos_list_1.append(list(pos))


pos = np.zeros(2)
pos_list_2 = [list(pos)]
cable = 1
for instruction in data[cable]:
    direction = instruction[0]
    length = int(instruction[1:])
    for l in range(length):
        pos += np.array(delta_pos[direction])
        pos_list_2.append(list(pos))


intersection = list(
    set(tuple(x) for x in pos_list_1).intersection(set(tuple(x) for x in pos_list_2))
)

t1 = []
t2 = []
for item in intersection:
    t1.append(pos_list_1.index(list(item)))
    t2.append(pos_list_2.index(list(item)))

print(np.min([item for item in np.array(t1) + np.array(t2) if item != 0]))
