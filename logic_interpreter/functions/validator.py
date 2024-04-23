from logic_interpreter.type import Type
from logic_interpreter.functions import operators

signals = {
    "=": operators.equal,
    "+": operators.add,
    "-": operators.sub,
    "*": operators.mul,
    "/": operators.truediv,
    "//": operators.floordiv,
    "%": operators.mod,
    "**": operators.pow,
    ">": operators.greater,
    "<": operators.less,
    ">=": operators.greaterEqual,
    "<=": operators.lessEqual,
}

def identify(obj1, signal, obj2):
    if signal in signals:
        obj1 = Type(obj1)
        obj2 = Type(obj2)
        result = signals[signal](obj1, obj2)
        print(result)
    else:
        return Exception