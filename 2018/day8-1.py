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
    
    def decreaseChildren(self):
        self.items[-2][0] -= 1
    
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



i = 0
metadata = 0
nodes = Stack()

while i < len(data):
    
    # Check whether top of stack has zero children
    if nodes.peekChildren() == 0:
        # Decrease children
        if nodes.size() > 1:
            nodes.decreaseChildren()
        
        # Add metadata
        nMetadata = nodes.peekMetadata()
        metadata += sum(data[i:i+nMetadata])
        i += nMetadata
        nodes.pop()

    else:
        # Add node
        nChildren = data[i]
        nMetadata = data[i+1]
        nodes.push([nChildren, nMetadata])
        i += 2
    
print(metadata)

