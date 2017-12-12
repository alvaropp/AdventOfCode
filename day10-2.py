
# coding: utf-8

# In[136]:

def solve(data, lengths, pos, skip):
    for length in lengths:
        if pos + length >= len(data):
            # Too long, wrap around!
            endPos = (pos + length) % len(data)
            span = (data[pos:] + data[:endPos])[::-1]
            data[pos:] = span[:len(data)-pos]
            data[:endPos] = span[len(data) - pos:]
        else:
            # Nice and short
            span = data[pos:pos+length][::-1]
            data[pos:pos+length] = span

        pos += length + skip
        pos = pos % len(data)
        skip += 1
    return data, pos, skip


# In[184]:

# Load input data
data = list(range(256))
with open("day10.txt") as f:
    lengths = f.readline().strip()

# Convert to ascii values
lengths = [ord(x) for x in lengths] + [17, 31, 73, 47, 23]

# State
pos = 0
skip = 0

# Iterate
for t in range(64):
    data, pos, skip = solve(data, lengths, pos, skip)
    
# Dense hash
dHash = []
for t in range(16):
    tempList = data[16*t:16*(t+1)]
    tempHash = 0
    for number in tempList:
        tempHash ^= number
    dHash.append(tempHash)

hexHash = ["{:02x}".format(number) for number in dHash]

print("Result =", "".join(hexHash))


# In[ ]:



