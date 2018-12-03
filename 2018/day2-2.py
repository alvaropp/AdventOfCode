with open('day2.txt') as f:
    data = f.read().splitlines()

for i, word1 in enumerate(data):
    for j, word2 in enumerate(data[i+1:]):
        diff = 0
        for k, letter1 in enumerate(word1):
            if letter1 != word2[k]:
                diff += 1
        if diff == 1:
            result1 = word1
            result2 = word2

result = []
for i, letter in enumerate(result1):
    if letter == result2[i]:
        result.append(letter)
print("".join(result))

