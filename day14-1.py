from day10_2 import computeHash

inputCode = "xlqgujun"
hashes = [computeHash(list(range(256)), inputCode + "-{}".format(i)) for i in range(128)]
binHashes = ["".join([bin(int(letter, 16))[2:].zfill(4) for letter in hash_]) for hash_ in hashes]
usedSquares = sum([binHashes[i].count('1') for i in range(len(binHashes))])

print("Result =", usedSquares)
