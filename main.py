import json
from logic_interpreter.logic import Logic
from logic_interpreter.type import Type
from logic_interpreter.stack import Stack
from logic_interpreter.functions.validator import identify

with open('data.json', 'r') as file:
    data = json.load(file)

t1 = Type("s")
t2 = Type("f")
t3 = Type("f")

print(t1 + t2)
print(t2 + t3)

print(t1 > t2)
print(t2 > t3)  

test = Logic(data)

print(test.ifObj.getPattern())

test = Stack(10)
test.add(20)
test.add(30)
test.add(40)

print(test.verify(30))
print(test.pop())
print(test.pop())
print(test.verify(30))
test.pop()
test.pop()
test.add(50)
print(test.pop())

test = Logic(data)

test.ifObj.interpreter()

identify(test, "+", test)