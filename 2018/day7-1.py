from collections import defaultdict


with open('day7.txt') as f:
    data = f.read().splitlines()


graph = defaultdict(list)
graphRev = defaultdict(list)
steps = []

for instruction in data:
    instruction = instruction.split(' ')
    steps.append(instruction[1])
    graph[instruction[1]].append(instruction[7])
    steps.append(instruction[7])
    graphRev[instruction[7]].append(instruction[1])
    
steps = set(steps)


notAvailable = set([item for sublist in graph.values() for item in sublist])
available = steps - notAvailable
available = sorted(list(available))
notAvailable = sorted(list(notAvailable))

orderedSteps = []
while len(available) != 0:
    # Remove the first available step and save it
    step = available.pop(0)
    orderedSteps.append(step)
    # Get the newly available steps
    for newStep in graph[step]:
        if (newStep not in orderedSteps) and (set(graphRev[newStep]).issubset(orderedSteps)):
            available.append(newStep)
    available = sorted(list(set(available)))

print("".join(orderedSteps))

