import numpy as np


with open("day24.txt") as f:
    data = [x.strip() for x in f.readlines()]

portA = [0] * len(data)
portB = [0] * len(data)
for i in range(len(data)):
    data_ = data[i].split('/')
    portA[i] = int(data_[0])
    portB[i] = int(data_[1])

adj = np.zeros([len(data), len(data)])
for i in range(len(data)):
    for j in list(range(0,i)) + list(range(i+1, len(data))):
        if (portA[i] in [portA[j], portB[j]]) and (portB[i] not in [portA[j], portB[j]]):
            adj[i, j] = 1
        if (portA[i] not in [portA[j], portB[j]]) and (portB[i] in [portA[j], portB[j]]):
            adj[i, j] = 2
        if (portA[i] in [portA[j], portB[j]]) and (portB[i] in [portA[j], portB[j]]):
            adj[i, j] = 3

def findConnections(i, freeSide):
    # Nodes
    nodes = list(np.where((adj[i] == freeSide) | (adj[i] == 3))[0])
    
    # Free sides
    if freeSide == 1:
        conn_i = int(portA[i])
    if freeSide == 2:
        conn_i = int(portB[i])
    freeSides = []
    for j in nodes:
        if portA[j] == conn_i:
            freeSides.append(2)
        elif portB[j] == conn_i:
            freeSides.append(1)
    connections = list(zip(nodes, freeSides))
    return connections

def DFS(i, freeSide):
    finals = []
    stacks = [[[i], findConnections(i, freeSide)]]
    
    while stacks:
        stack = stacks.pop(-1)
        bridge = stack[0]
        connections = stack[1]

        for conn in connections:
            if conn[0] not in bridge:
                newBridge = bridge + [conn[0]]
                newConn = findConnections(conn[0], conn[1])
                stacks.append([newBridge.copy(), newConn.copy()])
        if connections == []:
            finals.append(bridge)
    return finals

def computeStrength(bridge):
    strength = 0
    for node in bridge:
        strength += portA[node] + portB[node]
    return strength

startNodes = []
nodes_ = np.where(np.array(portA) == 0)[0]
for node in nodes_:
    startNodes.append((node, 2))
nodes_ = np.where(np.array(portB) == 0)[0]
for node in nodes_:
    startNodes.append((node, 1))

finals = []
for node in startNodes:
    i = node[0]
    side = node[1]
    finals.extend(DFS(i, side))

lens = np.array([len(x) for x in finals])
longests = np.where(lens == max(lens))[0]
strength = max([computeStrength(finals[ind]) for ind in longests])
print("Result =", strength)

