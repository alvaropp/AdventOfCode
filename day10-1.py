
# coding: utf-8

# In[110]:

def solve(data, lengths):
    pos = 0
    skip = 0
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
        print("Pos = {}, skip = {}".format(pos, skip))
        print("Data = ", data, '\n')
    return data


# In[120]:

data = list(range(256))
with open("day10.txt") as f:
    lengths = [int(x) for x in f.readline().strip().split(",")]

data = solve(data, lengths)

print("Result = ", data[0]*data[1])


# In[ ]:



