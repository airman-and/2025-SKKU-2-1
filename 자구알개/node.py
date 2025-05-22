class Node:
    def __init__(self, item):
        self.item = item # data field
        self.next = None # link field
# 멤버 변수 값 호출
    def get_item(self): return self.item

    def get_next(self): return self.next
# member variant value change
    def set_item(self,new_item):
        self.item = new_item
    
    def set_next(self, new_next):
        self.next = new_next

if __name__ == "__main__":
    a = Node(10)
    print(a.get_item())


