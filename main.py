import json
from logic_interpreter.logic import Logic

with open('data.json', 'r') as file:
    data = json.load(file)

test = Logic(data)

jsonData = {
    "if": test.ifObj.translateData
}

jsonData = json.dumps(jsonData, indent=4)

with open('response.json', 'w') as file:
    file.write(jsonData)