class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop()
        
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.items[len(self.items)-1]
    
    def peek(self): # return the top value
        if self.is_empty():
            return None
        else:
            return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
if __name__ == "__main__":

        s = Stack()
        print(s.is_empty())
        s.push(4)
        s.push('dog')
        print(s.peek())
        s.push(True)
        print(s.size())
        print(s.is_empty())
        s.push(8.4)
        print(s.pop())
        print(s.pop())
        print(s.size())
    