import json
from logic_interpreter.logic import Logic
from logic_interpreter.functions.validator import identify

with open('data.json', 'r') as file:
    data = json.load(file)

try:
    test = Logic(data)
    print(test.ifObj.translateData)
except:
    err = Exception("A error occurs")
    print(err)