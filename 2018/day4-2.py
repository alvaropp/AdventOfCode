import numpy as np
import dateutil.parser
from functools import partial
import operator


with open('day4.txt') as f:
    data = f.read().splitlines()

data.sort(key=lambda data: dateutil.parser.parse(data[1:17]))


sleep = {}

i = 0
while i < len(data):
    if data[i][19:24] == 'Guard':
        ID = int(data[i][26:].split(' ')[0])
        i += 1
        
        tmp = np.zeros(60)
        while i < len(data) and data[i][19:24] != 'Guard':
            if data[i][19] == 'f':
                t0 = int(data[i][15:17])
            elif data[i][19] == 'w':
                t1 = int(data[i][15:17])
                tmp[t0:t1] = np.ones(t1-t0)
            i += 1
        if ID in sleep.keys():
            sleep[ID] = np.vstack([sleep[ID], tmp])
        else:
            sleep[ID] = tmp


minuteCounts = {key: sum(sleep[key]) for key in sleep}
minute = np.argmax(minuteCounts[ID])

_max, _minute, _ID = 0, 0, 0
for ID, pattern in minuteCounts.items():
    try:
        ind = np.argmax(pattern)
        tmp = pattern[ind]

        if tmp > _max:
            _max = tmp
            _minute = ind
            _ID = ID
    except:
        pass

print(_ID*_minute)

