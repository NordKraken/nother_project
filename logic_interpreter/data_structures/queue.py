from logic_interpreter.data_structures.node import Node

class Queue:
    def __init__(self, value=None):
        self.first = Node(value)
        self.last = self.first
        self.size = 1

    def _setSize(self, value=1):
        if value == -1:
            self.size -= 1
        else:
            self.size += 1
    
    def __len__(self):
        return self.size
    
    def __repr__(self):
        return f"Queue()"
    
    def add(self, value):
        if self.first == None:
            self.first = Node(value)
            self.last = self.first
            self._setSize()
            return
        elif self.first.getValue() == None:
            self.first.setValue(value)
            return
        node = Node(value, self.last)
        self.last._setPointer(self.last.getNext(), node)
        self.last = node
        self._setSize()
    
    def show(self):
        self._getNodes(self.first)

    def _getNodes(self, node):
        if node == None:
            return
        print(node.getValue())
        self._getNodes(node.getBehind())

    def pop(self):
        if self.first == self.last:
            if self.first == None:
                return
            value = self.first.getValue()
            del self.first
            self.first = None
            self.last = self.first
            return value
        value = self.first.getValue()
        node = self.first
        self.first = self.first.getBehind()
        del node
        return value
    
    def verify(self, value):
        node = self.first
        while node != None:
            if node.getValue() == value:
                return True
            node = node.getBehind()
        return False