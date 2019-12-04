from collections import Counter
import numpy as np


start = 236491
stop = 713787

found = 0
for number in range(start, stop + 1):
    list_num = [int(num) for num in list(str(number))]
    value_count = [*Counter(list_num).values()]
    if (2 in value_count) & ((np.diff(list_num) >= 0).all()):
        found += 1

print(found)
