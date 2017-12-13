# Load input data
scanners = {}
positions = {}
directions = {}
with open("day13.txt") as f:
    for line in f.readlines():
        line = line.strip().split(": ")
        depth_ = int(line[0])
        range_ = int(line[1])
        scanners[depth_] = range_
        positions[depth_] = 0
        directions[depth_] = 1
maxDepth = depth_
scannersStart = scanners.copy()
positionsStart = positions.copy()
directionsStart = directions.copy()

# Brute force delays until not caught
for delay in range(20000000):
    player = -1
    caught = 0
    # Check whether caught
    scanners = scannersStart.copy()
    positions = positionsStart.copy()
    directions = directionsStart.copy()
    t = 0
    while t < maxDepth + 1 and not caught:
        # Jump to next layer
        player += 1
        # Check: have you been caught?
        if player in positions:
            if positions[player] == 0:
                # You have
                caught = 1
                break
        # Move scanners
        for pos in positions:
            if positions[pos] == 0:
                directions[pos] = 1
            if positions[pos] == scanners[pos]-1:
                directions[pos] = -1
            positions[pos] += directions[pos]
        # Update layer
        t += 1
    if not caught:
        print("===> Found, delay =", delay)
        break

    # Move scanners by one unit
    for pos in positions:
        if positionsStart[pos] == 0:
            directionsStart[pos] = 1
        if positionsStart[pos] == scannersStart[pos]-1:
            directionsStart[pos] = -1
        positionsStart[pos] += directionsStart[pos]
