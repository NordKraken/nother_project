flags = {
    "/n": "/n",
    "f": "f",
    "s": "s",
    "n": "n"
}

def parenteses(data):
    dataTwice = [[],"=",[]]
    encontred = False
    for i in data:
        if i == "=":
            encontred = True
            continue
        if encontred == False:
            dataTwice[0].append(i)
            continue
        dataTwice[2].append(i)
    dataTwice = [compacted(dataTwice[0]), dataTwice[1], compacted(dataTwice[2])]
    dataTwice[0] = analisy(dataTwice[0])
    dataTwice[2] = analisy(dataTwice[2])
    return (dataTwice[0] and dataTwice[2])

def compacted(data):
    value = ""
    for i in data:
        value += i
    return value

def analisy(data):
    if (
        ((flags["/n"] in data) or ((flags["f"] in data)
        or (flags["n"] in data)) and (flags["s"] in data))
    ):
        return False
    return True