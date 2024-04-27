import json
from logic_interpreter.logic import Logic
from logic_interpreter.functions.validator import identify
from logic_interpreter.data_structures.stack import Stack
from logic_interpreter.data_structures.queue import Queue

with open('data.json', 'r') as file:
    data = json.load(file)

test = Logic(data)

jsonData = {
    "if": test.ifObj.translateData
}

jsonData = json.dumps(jsonData, indent=4)

with open('response.json', 'w') as file:
    file.write(jsonData)