from logic_interpreter.type import Type

signals = {
    "=":1,
    "+":2,
    "-":3,
    "*":4,
    "/":5,
    "//":6,
    "%":7,
    "**":8,
    ">":0,
    "<":0,
    ">=":0,
    "<=":0,
}

def identify(obj1, signal, obj2):
    if signal in signals:
        print(signals[signal])
    else:
        return Exception