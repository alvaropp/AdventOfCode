from collections import Counter


with open("day6.txt") as f:
    data = [x.strip() for x in f.readlines()]

final = []
for i in range(len(data[0])):
    mssg = [line[i] for line in data]
    c = Counter(mssg)
    final.append(c.most_common(1)[0][0])

print("Result =", "".join(final))

