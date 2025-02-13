class LifoNode:
    def __init__(self, value):
        self.value = value
        self.next_value = None

class Lifo:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, value):
        new_node = LifoNode(value)
        new_node.next_value = self.top
        self.top = new_node
        self.size += 1
    
    def pop(self):
        if self.top is None:
            raise ValueError('Stack is empty')
        value = self.top.value
        self.top = self.top.next_value
        self.size -= 1
        return value
    
    def peek(self):
        if self.top is None:
            raise ValueError('Stack is empty')
        return self.top.value
    
    def is_empty(self):
        return self.top is None
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.top is None:
            return 'Stack is empty'
        result = []
        current = self.top
        while current:
            result.append(str(current.value))
            current = current.next_value
        return ' -> '.join(result[::-1])

lifo = Lifo()
lifo.push(1)
lifo.push(2)
lifo.push(3)
lifo.pop()
print(lifo)  