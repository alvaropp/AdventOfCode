with open('day8.txt') as f:
    data = f.read().splitlines()[0]
    data = [int(number) for number in data.split(' ')]


class Stack:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        return str(self.items)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
    def peekChildren(self):
        if self.size() > 0:
            return self.items[-1][0]
        else:
            return 9999
    
    def peekMetadata(self):
        if self.size() > 0:
            return self.items[-1][1]
        else:
            return 0

    def peekChildrenLeft(self):
        if self.size() > 0:
            return self.items[-1][2]
        else:
            return 9999

    def peekChildrenMetadata(self):
        if self.size() > 0:
            return self.items[-1][3]
        else:
            return None
    
    def decreaseChildren(self):
        self.items[-2][2] -= 1
    
    def addChildrenMetadata(self, metadata):
        self.items[-2][3].append(metadata)


i = 0
nodes = Stack()

while i < len(data):

    # Check whether top of stack has zero children
    if nodes.peekChildrenLeft() == 0:
        # Decrease children of parent
        if nodes.size() > 1:
            nodes.decreaseChildren()
        
        # Add metadata
        nMetadata = nodes.peekMetadata()
        # It had no children originally
        if nodes.peekChildren() == 0:
            lastMetadata = sum(data[i:i+nMetadata])
        # Had children originally
        else:
            lastMetadata = 0
            for ind in data[i:i+nMetadata]:
                if ind != 0:
                    try:
                        lastMetadata += nodes.peekChildrenMetadata()[ind-1]
                    except:
                        pass
        if nodes.size() > 1:
            nodes.addChildrenMetadata(lastMetadata)
        else:
            pass
        i += nMetadata
        tmp = nodes.pop()

    else:
        # Add node
        nChildren = data[i]
        nMetadata = data[i+1]
        nodes.push([nChildren, nMetadata, nChildren, []])
        i += 2
    
print(lastMetadata)

