class CircularListNode:
    def __init__(self, val, nex, prev):
        self.prev = prev
        self.val = val
        self.nex = nex

class CircularList:
    def __init__(self):
        self.head = None
        self.tail = None

    def unshift(self, value):
        if self.head is None:
            self.head = self.tail = CircularListNode(value, None, None)
        else:
            node = CircularListNode(value, self.head, None)
            self.head.prev = node
            self.tail.nex = node
            self.head = node

    def push(self, value):
        if self.head is None:
            self.head = self.tail = CircularListNode(value, None, None)
        else:
            node = CircularListNode(value, None, self.tail)
            self.tail.nex = node
            self.head.prev = node
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
            self.head.prev = self.tail 
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
            self.tail.nex = self.head 
        return result

    def forward(self):
        current = self.head

        while current is not None:
            yield current.val
            current = current.nex
            if current == self.head:
                break

    def backward(self):
        current = self.tail

        while current is not None:
            yield current.val
            current = current.prev
            if current == self.tail:
                break


circular_list = CircularList()
circular_list.push(5)
circular_list.unshift(10)

# for value in circular_list.forward():
#     print(value)

for value in circular_list.backward():
    print(value)
