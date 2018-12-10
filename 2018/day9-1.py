with open('day9.txt') as f:
    data = f.read().splitlines()[0].split(' ')
    nPlayers = int(data[0])
    nMarbles = int(data[6])


# Players
playerScores = [0] * nPlayers
currentPlayer = -1

# Marbles
right = [None] * nMarbles
left = [None] * nMarbles

# Initialise
current = 0
total = 1
right[current] = current
left[current] = current

for i in range(1, nMarbles):

    # Update player
    currentPlayer = (currentPlayer + 1) % nPlayers
    
    # Update marbles
    if i % 23 == 0:
        # Add new marble to score
        playerScores[currentPlayer] += i
        # Remove the 7th marble counterclockwise and keep
        marble7 = left[left[left[left[left[left[left[current]]]]]]]
        playerScores[currentPlayer] += marble7
        # Set new current
        current = right[marble7]
        # Redo the adjacency lists
        posLeft = left[marble7]
        posRight = right[marble7]
        right[posLeft] = posRight
        left[posRight] = posLeft
        right[marble7] = None
        left[marble7] = None

    else:
        posLeft = right[current]
        posRight = right[right[current]]
        right[posLeft] = i
        right[i] = posRight
        left[i] = posLeft
        left[posRight] = i
        current = i

print(max(playerScores))

