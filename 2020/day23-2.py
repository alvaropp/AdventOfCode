class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return repr(self.data)


class CircularDoublyLinkedList:
    def __init__(self, list):
        # Keep track of all the nodes to save look-up time
        self.nodes = {}

        # Head
        self.head = ListNode(data=list[0], next=list[0], prev=list[0])
        prev = self.head
        self.nodes[list[0]] = self.head

        # Load data
        for data in list[1:]:
            new = ListNode(data=data, prev=prev)
            self.nodes[data] = new
            prev.next = new
            prev = new

        new.next = self.head
        self.head.prev = new

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
            if curr == self.head:
                break
        return "[" + ", ".join(nodes) + "]"

    def find(self, key):
        return self.nodes.get(key, None)

    def remove(self, start_node, length=1):
        # build a circular sublist
        end_node = start_node
        removed_head = bool(start_node == self.head)
        for _ in range(length - 1):
            end_node = end_node.next
            if end_node == self.head:
                removed_head = True

        if removed_head:
            self.head = end_node.next

        # tie the ends of the remaining of the original list
        start_node.prev.next = end_node.next
        end_node.next.prev = start_node.prev

        return (start_node, start_node.next, end_node)

    def insert_after(self, node, start_node, end_node):
        node.next.prev = end_node
        end_node.next = node.next
        node.next = start_node
        start_node.prev = node


def solve(cups, n_rounds):
    curr = cups.head

    for _ in range(n_rounds):

        start_remove = curr.next
        to_remove = cups.remove(start_remove, length=3)
        removed_values = [node.data for node in to_remove]
        destination = curr.data
        while True:
            destination = (destination - 1) % (n_cups + 1)
            if destination in removed_values:
                continue
            elif destination > 0:
                destination_node = cups.find(destination)
                break

        cups.insert_after(destination_node, to_remove[0], to_remove[-1])

        curr = curr.next

    node = cups.find(1)
    result = 1
    for _ in range(2):
        node = node.next
        result *= node.data
    return result


n_cups = 1000000
n_rounds = 10000000

with open("day23.txt", "r") as f:
    data = list(map(int, list(f.read().strip())))
data.extend(range(len(data) + 1, n_cups + 1))

cups = CircularDoublyLinkedList(data)

print(solve(cups, n_rounds))
