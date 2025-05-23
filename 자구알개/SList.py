from node import Node
class SList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current !=None:
            count = count + 1
            current = current.get_next()
        return count 

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found: # found가 True가 될 때까지
            if current.get_item() == item:
                found = True
            else:
                current = current.get_next()
        return found
    
    def delete(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_item() ==item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())