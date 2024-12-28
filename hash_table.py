INITIAL_CAPACITY = 8


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    def _hash(self, key):
        hashsum = 0

        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum

    def insert(self, key, value):
        self.size += 1

        index = self._hash(key)
        node = self.buckets[index]

        if node is None:
            self.buckets[index] = Node(key, value)
            return

        prev = node
        while node:
            prev = node
            node = prev.next
        prev.next = Node(key, value)

    def delete(self, key):
        index = self._hash(key)
        node = self.buckets[index]

        prev = None
        while node and node.key != key:
            prev = node
            node = node.next


        if node is None:
            return None
        else:
            self.size -= 1
            prev.next = None



        return current.value

    def find(self, key):
        index = self._hash(key)
        node = self.buckets[index]
        if node is None:
            return None

        while node is not None and node.key != key:
            node = node.next

        return node.value


ht = HashTable()
ht.insert('a', 123)
ht.insert('b', 456)
ht.insert('c', 789)
ht.delete('a')

print(ht.find('b'))

