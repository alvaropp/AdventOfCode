with open('day5.txt') as f:
    data = f.read().splitlines()[0]


def cleanUp(data):
    result = []
    i = 0
    while i < len(data) - 1:
        if abs(ord(data[i+1]) - ord(data[i])) != 32:
            result.append(data[i])
            i += 1
        else:
            i += 2
    if abs(ord(data[-1]) - ord(data[-2])) != 32:
        result.append(data[-1])
    result = "".join(result)
    return result


finished = False
while not finished:
    dataNew = cleanUp(data)
    if len(dataNew) == len(data):
        finished = True
    else:
        data = dataNew

print(len(data))

