import hashlib


input_ = "abbhdwsy"

psswd = [0] * 8
hacked = [0] * 8
digit = 0
while sum(hacked) != 8:
    phrase = input_ + str(digit)
    hash_ = hashlib.md5(phrase.encode("utf-8")).hexdigest()
    if hash_[:5] == "00000":
        try:
            if (hacked[int(hash_[5])] == 0) and (int(hash_[5]) < 8) and (int(hash_[5]) >= 0):
                psswd[int(hash_[5])] = hash_[6]
                hacked[int(hash_[5])] = 1
        except:
            pass
    digit += 1
print("Solution =", "".join(psswd))

