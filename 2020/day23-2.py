# %%
def solve(cups, n_rounds):
    curr = cups.head
    for _ in range(n_rounds):

        start_remove = curr.next.data
        removed = cups.remove(start_remove, length=3)

        destination = curr.data
        while True:
            destination = (destination - 1) % (n_cups + 1)
            destination_node = cups.find(destination)
            if destination_node:
                break

        cups.insert_after(destination_node.data, removed)

        curr = curr.next

    result = ""
    node = cups.find(1)
    for _ in range(n_cups - 1):
        node = node.next
        result += f"{node.data}"
    return result


# %%
class ListNode:
    """
    A node in a singly-linked list.
    """

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class CircularLinkedList:
    def __init__(self, list):

        self.head = ListNode(data=list[0], next=list[0])
        prev = self.head

        for data in list[1:]:
            new = ListNode(data=data)
            prev.next = new
            prev = new

        new.next = self.head

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
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
            if curr == self.head:
                return None
        return curr

    def append(self, data):
        if not self.head:
            self.head = ListNode(data=data)
            return
        curr = self.head
        while (curr.next) and (curr.next != self.head):
            curr = curr.next
        curr.next = ListNode(data=data, next=self.head)

    def remove(self, key, length=1):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        # unlink `length` number of nodes from the list
        data_to_remove = [curr.data]
        if prev is None:
            last = self.head
            while True:
                if last.next == self.head:
                    break
                last = last.next

            for _ in range(length - 1):
                curr = curr.next
                data_to_remove.append(curr.data)
            self.head = curr.next
            last.next = self.head

        elif curr:
            crossed_head = False
            for _ in range(length - 1):
                curr = curr.next
                data_to_remove.append(curr.data)
                if curr == self.head:
                    crossed_head = True
            prev.next = curr.next
            if crossed_head:
                self.head = prev.next
        return data_to_remove

    def insert_after(self, key, data_list):
        node = self.find(key)
        prev = node
        old_next = prev.next
        for data in data_list:
            prev.next = ListNode(data=data)
            prev = prev.next
        prev.next = old_next


# %%
# n_cups = 1000000
n_rounds = 100

with open("test.txt", "r") as f:
    data = list(map(int, list(f.read().strip())))

n_cups = len(data)
# data.extend(range(len(data)+1, n_cups+1))

cups = CircularLinkedList(data)

solve(cups, n_rounds)
# %%
