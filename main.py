import json
from logic_interpreter import logic, type
from logic_interpreter import stack

with open('data.json', 'r') as file:
    data = json.load(file)

t1 = type.Type("s")
t2 = type.Type("f")
t3 = type.Type("f")

print(t1 + t2)
print(t2 + t3)

print(t1 > t2)
print(t2 > t3)  

test = logic.Logic(data)

print(test.ifObj.getPattern())

test = stack.Stack(10)
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