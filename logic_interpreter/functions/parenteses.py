def observer(data):
    compacted = ""
    while data:
        compacted += data[0]
        del data[0]
    return compacted