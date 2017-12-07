import itertools


result = 0

def checkPermInLine(words):
    for word in words:
        perms = ["".join(p) for p in itertools.permutations(word)]
        otherWords = [word_ for word_ in words if word_ is not word]
        for perm in perms:
            if perm in otherWords:
                return True
    return False

with open("day4.txt") as f:
    for line in f.readlines():
        words = line.strip().split(" ")
        if len(words) == len(set(words)) and not checkPermInLine(words):
            result += 1

print("Result = ", result)
