with open("day14.txt", 'r') as f:
    nIter = int(f.read().splitlines()[0])


def compute(nIter):
    
    scores = [3, 7]
    pos = [0, 1]
    
    while len(scores) < nIter + 10:
        scoreSum = scores[pos[0]] + scores[pos[1]]
        newScore = [scoreSum % 10] if scoreSum // 10 == 0 else [scoreSum // 10, scoreSum % 10]
        [scores.append(x) for x in newScore]
        pos[0] = (pos[0] + 1 + scores[pos[0]]) % len(scores)
        pos[1] = (pos[1] + 1 + scores[pos[1]]) % len(scores)
    
    extra = nIter + 10 - len(scores)
    if extra < 0:
        scores = scores[:extra]
    print(''.join(map(str, scores[-10:])))
    

compute(nIter)

