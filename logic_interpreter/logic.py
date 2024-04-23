from logic_interpreter.functions.validator import identify

class Logic:
    def __init__(self, data):
      if data["if"]:
        self.ifObj = Logic.If(data["if"])
        self.newIfData = []

    def __repr__(self):
      return "Logic class validator"

    class If:
      def __init__(self, ifData):
        self.ifData = ifData

      def delElement(self):
        if self.ifData:
          del self.ifData[0]
      
      def interpreter(self):
        if not self.ifData:
          return
        pattern = self.getPattern()
        self.delElement()
        if "(" in pattern or ")" in pattern:
          self.solveParanteses()
        else:
          self.translate(pattern[0], pattern[1], pattern[2])

      def translate(self, p1, signal, p2):
        identify(p1, signal, p2)

      def solveParanteses(self):
        pass

      def getPattern(self):
        if self.ifData:
          pattern = self.ifData[0]
          pattern = [s for s in pattern]
          return pattern
        return None
      
      def __len__(self):
        return len(self.ifData)

      def __repr__(self):
        return "If class validator"