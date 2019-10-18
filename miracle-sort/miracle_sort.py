def is_sorted(data):
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True

def miraclesort(data):
    while not is_sorted(data):
        pass
    return data

myList = [5,1,8,2,4,32,8,42,2]
miraclesort(myList)