with open('2018/day2.txt') as f:
    data = f.read().splitlines()

n2 = 0
n3 = 0

for word in data:
    aset = set(word)    
    n2tmp = 0
    n3tmp = 0
    for letter in aset:
        if word.count(letter) == 2:
            n2tmp = 1
        if word.count(letter) == 3:
            n3tmp = 1
    n2 += n2tmp
    n3 += n3tmp

print(n2*n3)
