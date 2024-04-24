import json
from logic_interpreter.logic import Logic
from logic_interpreter.functions.validator import identify
from logic_interpreter.stack import Stack

with open('data.json', 'r') as file:
    data = json.load(file)

try:
    test = Logic(data)
    print(test.ifObj.translateData)
except:
    err = Exception("A error occurs")
    print(err)

a = Stack(10)
a.add(20)
a.add(30)
a.add(40)
a.add(50)

a.show()