import json
from logic_interpreter.logic import Logic
from logic_interpreter.functions.validator import identify
from logic_interpreter.data_structures.stack import Stack
from logic_interpreter.data_structures.queue import Queue

with open('data.json', 'r') as file:
    data = json.load(file)

try:
    test = Logic(data)
    print(test.ifObj.translateData)
except:
    err = Exception("A error occurs on main")
    print(err)