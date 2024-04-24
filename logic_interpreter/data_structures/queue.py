from logic_interpreter.data_structures.node import Node

class Queue:
    def __init__(self, value):
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
    
    def add(self, value):
        if self.first == None:
            self.first = Node(value)
            self.last = self.first
            self._setSize()
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