class Node:
    def __init__(self, value, pointer=None):
        self.value = value
        self.pointer = pointer    
    
    def setPointer(self, pointer):
        self.pointer = pointer

    def getNext(self):
        return self.pointer
    
    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

class Stack:
    def __init__(self, value):
        self.last = Node(value)
        self.first = self.last
        self.size = 1

    def __len__(self):
        return self.size
    
    def setSize(self, value=1):
        if value == 1:
            self.size += 1
        elif self.size == -1:
            self.size -= 1
    
    def add(self, value):
        if self.first == self.last:
            self.first = Node(value, self.last)
            self.setSize()
            return
        node = Node(value, self.first)
        self.first = node
        self.setSize()
    
    def pop(self):
        if self.first == self.last:
            value = self.first.getValue()
            del self.first
            self.first = None
            self.last = None
            self.setSize(-1)
            return value
        node = self.first
        self.first = self.first.getNext()
        value = node.getValue()
        del node
        self.setSize(-1)
        return value
    
    def verify(self, value):
        node = self.first
        while node != None:
            if node.getValue() == value:
                return True
            node = node.getNext()
        return False