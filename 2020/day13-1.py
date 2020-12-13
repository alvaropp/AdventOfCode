with open("day13.txt", "r") as f:
    data = f.read().splitlines()

earliest = int(data[0])
ids = [int(id) for id in data[1].split(",") if id != "x"]

timestamp = earliest

found = False
while not found:
    for id_ in ids:
        if timestamp % id_ == 0:
            found = True
            break
    timestamp += 1

print((timestamp - earliest - 1) * id_)
