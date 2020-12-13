# Didn't manage to solve part 2 (in finite time, that is) so had a look
# at the megathread in Reddit to re-discover the Chinese reminder theorem :)

with open("day13.txt", "r") as f:
    ids = f.read().splitlines()[1].split(",")

offsets = []
valid_ids = []
for offset, id in enumerate(ids):
    if id != "x":
        valid_ids.append(int(id))
        offsets.append(offset)


def solve(ids, offsets):
    """Chinese reminder theorem."""
    N = 1
    for id in ids:
        N *= id

    t = 0
    for id, offset in zip(ids, offsets):
        ni = N // id
        inv = pow(ni, -1, id)
        t -= offset * ni * inv

    return t % N


print(solve(valid_ids, offsets))
