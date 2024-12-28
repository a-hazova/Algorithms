class DLinkedListNode:
    def __init__(self, val, nex, prev):
        self.prev = prev
        self.val = val
        self.nex = nex


class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def unshift(self, value):
        if self.head is None:
            self.head = self.tail = DLinkedListNode(value, None, None)
        else:
            node = DLinkedListNode(value, self.head, None)
            self.head.prev = node
            self.head = node

    def push(self, value):
        if self.head is None:
            self.head = self.tail = DLinkedListNode(value, None, None)
        else:
            node = DLinkedListNode(value, None, self.tail)
            self.tail.nex = node
            self.tail = node

    def shift(self):
        if self.head is None:
            raise ValueError('List is empty')
        result = self.head.val
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.nex
            self.head.prev = None
        return result

    def pop(self):
        if self.head is None:
            raise ValueError('List is empty')
        result = self.tail.val
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.nex = None
        return result

    def forward(self):
        current = self.head

        while current is not None:
            yield current.val
            current = current.nex

    def backward(self):
        current = self.tail

        while current is not None:
            yield current.val
            current = current.prev

    def get(self, index):






dlist = DLinkedList()
dlist.unshift(4)
dlist.push(5)
dlist.unshift(3)
dlist.push(6)
print(sum(dlist.forward()))
