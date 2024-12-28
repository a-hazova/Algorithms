
class LinkedListNode:
    def __init__(self, elem, next_elem):
        self.elem = elem
        self.link = next_elem


class LinkedList2:
    def __init__(self):
        self.head = None

    def find(self, value):
        current = self.head
        while current is not None:
            if current.elem == value:
                return True
            current = current.link
        return False

    def length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.link
        return count

    def insert(self, index, value):
        if self.head is None:
            self.head = LinkedListNode(value, None)
        elif index == 0:
            self.unshift(value)
        else:
            current = self.head
            while current.link is not None and index > 1:
                current = current.link
                index -= 1
            current.link = LinkedListNode(value, current.link)

    def shift(self):
        value = self.head.elem
        self.head = self.head.link
        return value

    def unshift(self, elem):  # алг.сложность O(1)
        self.head = LinkedListNode(elem, self.head)

    def pop(self):
        current = self.head
        prev = None
        while current.link is not None:
            prev = current
            current = current.link
        prev.link = None
        return current.elem

    def delete(self, index):
        if self.head is None:
            return None
        elif index == 0:
            return self.shift()
        else:
            current = self.head
            while current.link.link is not None and index > 1:
                current = current.link
                index -= 1
            value = current.link.elem
            current.link = current.link.link
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
            yield current.value
            current = self.head.link


llist = LinkedList2()
llist.unshift(1)
llist.unshift(2)
llist.unshift(3)
