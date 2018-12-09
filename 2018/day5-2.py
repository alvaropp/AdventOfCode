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

def compress(unit, dataOld):
    dataOld = dataOld.replace(unit, '')
    dataOld = dataOld.replace(unit.upper(), '')
    
    finished = False
    while not finished:
        dataNew = cleanUp(dataOld)
        if len(dataNew) == len(dataOld):
            finished = True
        else:
            dataOld = dataNew
    return len(dataNew)


results = {}
for letter in set(data.lower()):
    length = compress(letter, data)
    results[letter] = length

print(results[min(results, key=results.get)])

