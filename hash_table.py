INITIAL_CAPACITY = 8


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_value = None


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
        index = self._hash(key)
        node = self.buckets[index]

        if node is None:
            self.buckets[index] = Node(key, value)
            self.size += 1
            return
        else:
            current = self.buckets[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next_value

            new_node = Node(key, value)
            new_node.next_value = node
            self.buckets[index] = new_node
            self.size += 1

    def delete(self, key):
        index = self._hash(key)
        node = self.buckets[index]

        prev = None
        while node and node.key != key:
            prev = node
            node = node.next_value

        if node is None:
            raise KeyError(f'No key "{key}" found')
        else:
            self.size -= 1
            prev.next_value = node.next_value

        return node.value

    def find(self, key):
        index = self._hash(key)
        node = self.buckets[index]
        while node:
            if node.key == key:
                return True
            node = node.next_value
        return False
    
    def get(self, key, default=None):
        index = self._hash(key)
        node = self.buckets[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next_value
        return default

    def setDefault(self, key, default=None):
        index = self._hash(key)
        node = self.buckets[index]

        current = self.buckets[index]
        while current:
            if current.key == key:
                return current.value 
            current = current.next_value
        new_node = Node(key, default)
        new_node.next_value = node
        self.buckets[index] = new_node
        return default
        

ht = HashTable()
ht.insert('a', 123)
ht.insert('b', 567)
ht.insert('c', 456)
print(ht.setDefault('d', "uiu"))
print(ht.get('d'))

