from dataclasses import dataclass


@dataclass
class Node:
    x: int
    y: int
    size: int
    used: int
    avail: int


with open("day22.txt", "r") as f:
    data = f.read().splitlines()

nodes = []
for line in data[2:]:
    name, size, used, avail, _ = line.split()
    x, y = name.split("-")[1:]
    nodes.append(
        Node(int(x[1:]), int(y[1:]), int(size[:-1]), int(used[:-1]), int(avail[:-1]))
    )

viable_pairs = 0
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        if nodes[i].used != 0 and nodes[i].used <= nodes[j].avail:
            viable_pairs += 1
        elif nodes[j].used != 0 and nodes[j].used <= nodes[i].avail:
            viable_pairs += 1

print(viable_pairs)

