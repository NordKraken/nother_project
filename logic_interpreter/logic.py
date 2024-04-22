class Logic:
    def __init__(self, data):
      if data["if"]:
        self.ifObj = Logic.If(data["if"])
        self.newIfData = []

    def __repr__(self):
      return "Logic class validator"
    
    def interpreter(self):
      if self.ifObj.ifData:
        pattern = self.ifObj.getPattern()

    class If:
      def __init__(self, ifData):
        self.ifData = ifData
      
      def getPattern(self):
        if self.ifData:
          pattern = self.ifData[0]
          del self.ifData[0]
          pattern = [s for s in pattern]
          return pattern
        return None
      
      def __len__(self):
        return len(self.ifData)

      def __repr__(self):
        return "If class validator"