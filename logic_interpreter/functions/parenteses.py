from logic_interpreter.data_structures.queue import Queue

def observer(data):
    compacted = ""
    while data:
        compacted += data[0]
        del data[0]
    return compacted