from dataclasses import dataclass


@dataclass
class Node:
    size: int
    used: int
    avail: int


with open("day22.txt", "r") as f:
    data = f.read().splitlines()

nodes = {}
for line in data:
    name, size, used, avail, _ = line.split()
    x, y = name.split("-")[1:]
    nodes[(int(x[1:]), int(y[1:]))] = Node(
        int(size[:-1]), int(used[:-1]), int(avail[:-1])
    )
pprint = ""
for i in range(max(nodes, key=lambda node: node[1])[1] + 1):
    for j in range(max(nodes, key=lambda node: node[0])[0] + 1):
        node = nodes[(j, i)]
        if (j, i) == (0, 0):
            pprint += "E "
        elif (j, i) == (max(nodes, key=lambda node: node[0])[0], 0):
            pprint += "S "
        elif node.used == 0:
            empty_node = (j, i)
            pprint += "O "
        elif node.used / node.size > 0.9:
            pprint += "# "
        else:
            pprint += ". "
    pprint += "\n"

print(pprint)
print(f"empty node: {empty_node}")
print(
    f"size: {max(nodes, key=lambda node: node[1])[1]}, {max(nodes, key=lambda node: node[0])[0]}"
)
