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
    dataTwice = (compacted(dataTwice[0]), dataTwice[1], compacted(dataTwice[2]))
    print(dataTwice)

def compacted(data):
    value = ""
    for i in data:
        value += i
    return value