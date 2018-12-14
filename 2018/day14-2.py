with open("day14.txt", 'r') as f:
    nIter = f.read().splitlines()[0]


def compute(nIter):
    
    pattern = [int(n) for n in str(nIter)]

    scores = [3, 7]
    pos = [0, 1]
    
    while (scores[-len(pattern):] != pattern) and (scores[-len(pattern)-1:-1] != pattern):
        scoreSum = scores[pos[0]] + scores[pos[1]]
        newScore = [scoreSum % 10] if scoreSum // 10 == 0 else [scoreSum // 10, scoreSum % 10]
        scores.extend(newScore)
        pos[0] = (pos[0] + 1 + scores[pos[0]]) % len(scores)
        pos[1] = (pos[1] + 1 + scores[pos[1]]) % len(scores)
    
    print(len(scores) - len(pattern) - (0 if scores[-len(pattern):] == pattern else 1))


compute('825401')

