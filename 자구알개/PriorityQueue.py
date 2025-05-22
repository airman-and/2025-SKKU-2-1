from node import Node
class PriorityQueue:

    def __init__(self):
        self.head = None

# 시간복잡도 O(N)
    def enqueue(self, item):
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

# 시간복잡도 O(1)
    def deaueue(self):
        if self.head == None:
            return None
        else:
            temp = self.head
            dequeued_item = temp.get_item()
            self.head = self.head.get_next()
            return dequeued_item
        
# 힙을 이용한 우선순위 큐 구현
# 우선순위 큐는 현재 우선순위가 가장 높은 항목을 하나씩 삭제 및 반환하는 목적으로 사용
# 현재 우선순위가 가장 높은 항목을 하나씩 삭제 및 반환할 경우 모든 항목을 정렬시킬 필요가 없음
