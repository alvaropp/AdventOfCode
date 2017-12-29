names = []
children = []
with open("day7.txt") as f:
    for line in f.readlines():
        data = line.split('->')
        names.append(data[0].split(" ")[0])
        if len(data) == 2:
            [x.strip() for x in data[1].split(',')]
            children.append([x.strip() for x in data[1].split(',')])
children = [element for sublist in children for element in sublist]

print("Result = ", [x for x in names if x not in children])
