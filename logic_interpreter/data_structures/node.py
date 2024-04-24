class Node:
    def __init__(self, value, fp=None, bp=None):
        self.value = value
        self.fp = fp
        self.bp = bp
    
    def _setPointer(self, fp, bp):
        self.fp = fp
        self.bp = bp

    def getNext(self):
        return self.fp
    
    def getBehind(self):
        return self.bp
    
    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value