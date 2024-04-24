from logic_interpreter.functions.validator import identify

class Logic:
    def __init__(self, data):
      if data["if"]:
        self.ifObj = Logic.If(data["if"])

    def __repr__(self):
      return "Logic class validator"

    class If:
      def __init__(self, ifData):
        self.ifData = ifData
        self.translateData = []
        self._interpreter()

      def _delElement(self):
        if self.ifData:
          del self.ifData[0]
      
      def _interpreter(self):
        if not self.ifData:
          return
        while self.ifData:
          pattern = self._getPattern()
          self._delElement()
          if "(" in pattern or ")" in pattern:
            self._solveParanteses()
          else:
            self._translate(pattern[0], pattern[1], pattern[2])

      def _translate(self, p1, signal, p2):
        self.translateData.append(identify(p1, signal, p2))

      def _solveParanteses(self):
        pass

      def _getPattern(self):
        if self.ifData:
          pattern = self.ifData[0]
          pattern = [s for s in pattern]
          return pattern
        return None
      
      def __len__(self):
        return len(self.ifData)

      def __repr__(self):
        return "If class validator"