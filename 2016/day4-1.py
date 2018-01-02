from collections import Counter
import numpy as np


with open("day4.txt") as f:
    data = [x.strip() for x in f.readlines()]

IDs = []
for name in data:
    name_ = "".join(name.split('-')[:-1])
    ID = int(name.split('-')[-1].split('[')[0])
    checksum = name.split('-')[-1].split('[')[1][:-1]

    # Top 5
    word_counts = Counter(list(name_))
    top_ = word_counts.most_common(30)
    top_counts = np.array([pair[1] for pair in top_])
    top_letters = np.array([pair[0] for pair in top_])

    # Sort
    checksum_ = []
    for i in list(set(top_counts))[::-1]:
        ind = np.where(top_counts == i)[0]
        checksum_.append(sorted(top_letters[ind]))
    checksum_ = "".join([item for sublist in checksum_ for item in sublist])
    # Check
    if checksum_[:5] == checksum:
        IDs.append(ID)

print("Result =", sum(IDs))

