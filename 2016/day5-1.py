import hashlib


input_ = "abbhdwsy"

psswd = []
digit = 0
while len(psswd) < 8:
    phrase = input_ + str(digit)
    hash_ = hashlib.md5(phrase.encode("utf-8")).hexdigest()
    if hash_[:5] == "00000":
        psswd.append(hash_[5])
    digit += 1
print("Solution =", "".join(psswd))

