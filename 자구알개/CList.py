from node import Node
class CList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        if self.is_empty():
            temp.set_next(temp)
            self.head = temp
        else:
            temp.set_next(self.head.get_next())
            self.head.set_next(temp)
        
    def append(self, item):
        temp = Node(item)
        if self.is_empty():
            temp.set_next(temp)
            self.head = temp
        else:
            temp.set_next(self.head.get_next())
            self.head.set_next(temp)
            self.head = temp #head를 temp 에 옮겨야 temp의 노드가 마지막 값으로 append된다.
    
    def pop_first(self):
        if self.head == None:
            print("List is empty.")
        else:
            temp = self.head.get_next()
            if temp == temp.get_next():
                self.head = None
            else:
                self.head.set_next(temp.get_next())
    
    def search(self, item):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head.get_next()
            if self.head == temp:
                if self.head.get_item == item:
                    return True
                else:
                    return False
            found = False
            current = temp
            while True:
                if current.get_item() == item:
                    found = True
                else:
                    current = current.get_next()
                if current != temp and not found:
                    continue
                else:
                    break
        return found