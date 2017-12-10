import numpy as np
import copy


def loadInput(filename):
    names = []
    weightsDict = {}
    children = []
    childrenDict = {}
    with open(filename) as f:
        for line in f.readlines():
            data = line.split('->')
            names.append(data[0].split(" ")[0])
            weightsDict[data[0].split(" ")[0]] = int(data[0].split("(")[1].split(")")[0])
            if len(data) == 2:
                [x.strip() for x in data[1].split(',')]
                children.append([x.strip() for x in data[1].split(',')])
                childrenDict[data[0].split(" ")[0]] = [x.strip() for x in data[1].split(',')]
            if len(data) == 1:
                childrenDict[data[0].split(" ")[0]] = []
    children = [element for sublist in children for element in sublist]
    base = [x for x in names if x not in children][0]
    
    return names, weightsDict, base, childrenDict

def buildTree(base, childrenDict, weightsDict):
    tree = []; wTree = []; layer = [];
    tree.append([base])
    layer.append(base)
    while layer:
        temp = []; wTemp = [];
        for element in layer:
            temp.append(childrenDict[element])
            wTemp.append(weightsDict[element])
        layer = []
        tree.append(temp)
        wTree.append(wTemp)
        layer += [x for sublist in temp for x in sublist]
    return tree, wTree

def buildCumulativeWeights(tree, wTree):
    cumWTree = copy.deepcopy(wTree)
    badBranch = False
    for depth in range(len(tree)-2, 0, -1):
        w0 = 0; wf = 0;
        ind = 0
        for i, branch in enumerate(tree[depth]):
            # Back-propagate
            for j, element in enumerate(branch):
                cumWTree[depth-1][i] += cumWTree[depth][ind]
                ind += 1
    return cumWTree

names, weightsDict, base, childrenDict = loadInput("day7.txt")
tree, wTree = buildTree(base, childrenDict, weightsDict)
cumWTree = buildCumulativeWeights(tree, wTree)

# Solve
found = False
for depth in range(len(tree)-2, 0, -1):
    if not found:
        s = 0; f = 0;
        for branch in tree[depth]:
            f += len(branch)
            # Check whether all the weights are the same
            ws = cumWTree[depth][s:f]
            orWs = wTree[depth][s:f]
            if not(ws[1:] == ws[:-1]):
                found = True
                break
            s = f

ws = np.array(ws); orWs = np.array(orWs);
ws_ = list(set(ws))

if len((ws == ws_[0])) == 1:
    rest = ws_[1]
    different = ws_[0]
else:
    rest = ws_[0]
    different = ws_[1]

difference = rest - different
pos = np.where(ws == different)[0][0]
result = orWs[pos] + difference

print("Result = ", result)

