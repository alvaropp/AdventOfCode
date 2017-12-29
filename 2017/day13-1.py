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

# Set player position
player = -1
# Severity
severity = 0

for t in range(depth_ + 1):
    # Jump to next layer
    player += 1
    # Check: have you been caught?
    if player in positions:
        if positions[player] == 0:
            # You have
            severity += player*scanners[player]
    # Move scanners
    for pos in positions:
        if positions[pos] == 0:
            directions[pos] = 1
        if positions[pos] == scanners[pos]-1:
            directions[pos] = -1
        positions[pos] += directions[pos]

print("Severity =", severity)
