class Type:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "Type of the parameter value"

    def validador(self, value):
        if self.value == "n":
            self.value == "f"
        if value == "n":
            value = "f"
        if self.value != value:
            return False
        return True

    def __add__(self, obj):
        return self.validador(obj.value)
    
    def __sub__(self, obj):
        return self.validador(obj.value)
    
    def __mul__(self, obj):
        if self.value != "s" and obj.value != self.value:
            return self.validador(obj.value)
        return False
    
    def __truediv__(self, obj):
        if self.value != "s" and obj.value != self.value or obj.value != "n":
            return self.validador(obj.value)
        return False
    
    def __mod__(self, obj):
        if self.value != "s" and obj.value != self.value or obj.value != "n":
            return self.validador(obj.value)
        return False
    
    def __floordiv__(self, obj):
        if self.value != "s" and obj.value != self.value or obj.value != "n":
            return self.validador(obj.value)
        return False
    
    def __pow__(self, obj):
        if self.value != "s" and obj.value != self.value:
            return self.validador(obj.value)
        return False
    
    def convertBase(self, obj):
        if self.value == "f" or self.value == "n":
            self.value == "s"
        if obj.value == "f" or obj.value == "n":
            obj.value == "s"

    def __eq__(self, obj):
        self.convertBase(obj)
        return self.validador(obj.value)
    
    def __le__(self, obj):
        self.convertBase(obj)
        return self.validador(obj.value)
    
    def __lt__(self, obj):
        self.convertBase(obj)
        return self.validador(obj.value)
    
    def __ne__(self, obj):
        self.convertBase(obj)
        return self.validador(obj.value)
    
    def __ge__(self, obj):
        self.convertBase(obj)
        return self.validador(obj.value)
    
    def __gt__(self, obj):
        self.convertBase(obj)
        return self.validador(obj.value)