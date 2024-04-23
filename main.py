import json
from logic_interpreter.logic import Logic
from logic_interpreter.type import Type
from logic_interpreter.stack import Stack
from logic_interpreter.functions.validator import identify

with open('data.json', 'r') as file:
    data = json.load(file)

try:
    identify("f", "=", "f")
except:
    err = Exception("A error occurs")
    print(err)