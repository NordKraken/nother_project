from logic_interpreter.data_structures.queue import Queue

def observer(data):
    struturedData = Queue()
    for i in data:
        struturedData.add(i)
    struturedData.show()
    return struturedData