filename = "day9.txt"
with open(filename) as f:
    data = f.readlines()[0].strip()

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
    deleted = 0
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
        # Keep track of the number of deleted items
        deleted += (end - start - 1)

    # Clean all ","s
    data = data.replace(",", "")
    return data, deleted

data, deleted = process(data)
print("Deleted = ", deleted)
