from logic_interpreter.data_structures.node import Node

class Stack:
    def __init__(self, value=None):
        self.last = Node(value)
        self.first = self.last
        self.size = 1

    def __len__(self):
        return self.size
    
    def __repr__(self):
        return "Stack()"
    
    def _setSize(self, value=1):
        if value == 1:
            self.size += 1
        elif self.size == -1:
            self.size -= 1
    
    def add(self, value):
        if self.first == self.last:
            if self.first.getValue() == None:
                self.first.setValue(value)
                return
            self.first = Node(value, self.last)
            self._setSize()
            return
        node = Node(value, self.first)
        self.first = node
        self._setSize()
    
    def pop(self):
        if self.first == self.last:
            if self.first == None:
                return
            value = self.first.getValue()
            del self.first
            self.first = None
            self.last = None
            self._setSize(-1)
            return value
        node = self.first
        self.first = self.first.getNext()
        value = node.getValue()
        del node
        self._setSize(-1)
        return value
    
    def verify(self, value):
        node = self.first
        while node != None:
            if node.getValue() == value:
                return True
            node = node.getNext()
        return False
    
    def show(self):
        self._getNodes(self.first)

    def _getNodes(self, node):
        if node == None:
            return
        print(node.getValue())
        self._getNodes(node.getNext())