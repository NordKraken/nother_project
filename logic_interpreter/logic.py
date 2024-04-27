from logic_interpreter.functions.validator import identify
from logic_interpreter.functions.parenteses import parenteses
class Logic:
    def __init__(self, data):
      if data["if"]:
        self.ifObj = Logic.If(data["if"])

    def __repr__(self):
      return "Logic(data)"

    class If:
      def __init__(self, ifData):
        self.ifData = ifData
        self.translateData = []
        self._interpreter()

      def __repr__(self):
        return f"If({self.ifData})"

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
            self._solveParanteses(pattern)
          else:
            self._translate(pattern[0], pattern[1], pattern[2])

      def _translate(self, p1, signal, p2):
        self.translateData.append(identify(p1, signal, p2))

      def _solveParanteses(self, pattern):
        self.translateData.append(parenteses(pattern))

      def _getPattern(self):
        if self.ifData:
          pattern = self.ifData[0]
          pattern = [s for s in pattern]
          return pattern
        return None
      
      def __len__(self):
        return len(self.ifData)