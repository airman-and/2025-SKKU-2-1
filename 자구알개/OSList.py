from node import Node

def add(self,item):
    current = self.head
    previous = None
    stop = False
    while current != None and not stop:
        if current.get_item() > item:
            stop = True
        else:
            previous = current
            current = current.get_next()
    temp = Node(item)
    if previous == None:
        temp.set_next(self.head)
        self.head = temp
    else:
        temp.set_next(current)
        previous.set_next(temp)


def search(self,item):
    current = self.head
    found = False
    stop = False
    while current != None and not stop and not found:
        if current.get_item() == item:
            found = True
        else:
            if current.get_item() > item:
                stop = True
            else:
                current = current.get_next()
    return found