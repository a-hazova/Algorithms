
class LinkedListNode:
    def __init__(self, elem, next_elem):
        self.elem = elem
        self.link = next_elem


class LinkedList:
    _length = 0
    def __init__(self):
        self.head = None
        self.tail = None

    def find(self, value):
        current = self.head
        while current is not None:
            if current.elem == value:
                return True
            current = current.link
        return False
    
    @property
    def length(self):
        return self._length
    
    def insert(self, index, value):
        if self.head is None:
            self.head = LinkedListNode(value, None)
            self.tail = self.head
           
        elif index == 0:
            self.unshift(value)
        else:
            current = self.head
            while current.link is not None and index > 1:
                current = current.link
                index -= 1
            current.link = LinkedListNode(value, current.link)
        self._length += 1

    def shift(self):
        value = self.head.elem
        self.head = self.head.link
        self._length -= 1
        return value

    def unshift(self, elem):  # алг.сложность O(1)
        previous = self.head
        self.head = LinkedListNode(elem, self.head)
        if previous is None:
            self.tail = self.head
        self._length += 1

    def pop(self):
        current = self.head
        prev = None
        while current.link is not None:
            prev = current
            current = current.link
        prev.link = None
        self.tail = prev
        self._length -= 1
        return current.elem
    
    def push(self, elem):
        if self.head is None:
            self.head = LinkedListNode(elem, None)
            self.tail = self.head
        else:
            self.tail.link = LinkedListNode(elem, None)
            self.tail = self.tail.link
        self._length += 1

    def delete(self, index):
        if index >= self.length:
            raise IndexError("Index out of range")
        if self.head is None:
            return None
        elif index == 0:
            return self.shift()
        elif index == self.length - 1:
            return self.pop()
        else:
            current = self.head
            while current.link is not None and index > 1:
                current = current.link
                index -= 1
            value = current.link.elem
            current.link = current.link.link
            self._length -= 1
            return value

    def get(self, index):
        if self.head is None:
            return None
        elif index == 0:
            return self.head.elem
        else:
            current = self.head
            while current.link is not None and index > 0:
                current = current.link
                index -= 1
            return current.elem

    def update(self, old_value, new_value):
        if self.head is None:
            self.head = LinkedListNode(new_value, None)
        else:
            current = self.head
            while current is not None:
                if current.elem == old_value:
                    current.elem = new_value
                    return new_value
                current = current.link
            raise ValueError(f'No element found with value: {old_value}')

    def map(self, func):
        if self.head is None:
            raise ValueError("List is empty")
        current = self.head
        while current:
            current.elem = func(current.elem)
            current = current.link

    def reduce(self, func, initial = None):
        if self.head is None:
            raise ValueError("List is empty")

        if initial is None:
            initial = self.head.elem

        current = self.head.link
        accumulator = initial
        while current:
            accumulator = func(accumulator, current.elem)
            current = current.link
        return accumulator

    def iterate(self):
        current = self.head

        while current is not None:
            yield current.elem
            current = current.link


llist = LinkedList()
llist.unshift(1)
llist.unshift(2)
llist.unshift(3)
llist.pop()
llist.push(5)
llist.delete(0)

sum = llist.reduce(func = lambda a, c: a + c)

for i in llist.iterate():
    print(i) 

print(f'Длина списка: {llist.length}')