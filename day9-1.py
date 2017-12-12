
# coding: utf-8

# In[46]:

data = "{{<a!>},{<a!>},{<a!>},{<ab>}}"


# In[49]:

filename = "day9.txt"
with open(filename) as f:
    data = f.readlines()[0].strip()


# In[50]:

def process(data):
    dataClean = ""
    # Delete things after "!"s
    i = 0
    while i < len(data):
        if data[i] == "!":
            pass
            i += 2
        else:
            dataClean += data[i]
            i += 1
    data = dataClean

    # Delete things inside "<", ">" pairs
    oldData = ""
    while oldData is not data:
        oldData = data
        try:
            start = data.index("<")
            end = data.index(">")
        except:
            break
        dataL = list(data)[:start] + list(data)[end+1:]
        data = "".join(dataL)
    
    # Clean all ","s
    data = data.replace(",", "")
    return data

data = process(data)
print("Data = ", data)

def score(data):
    score = 0
    open_ = 0
    close_ = 0
    for c in data:
        if c == "{":
            open_ += 1
        if c == "}":
            score += open_
            open_ -= 1
    return score

print("Score = ", score(data))


# In[ ]:



