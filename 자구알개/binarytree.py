from btnode import Node
from clqueue import queue

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def preorder(self, node):
        if node != Node:
            print(str(node.get_key()),' ',end='')
            if node.get_left():
                self.preorder(node.get_left())
            if node.get_right():
                self.preorder(node.get_right())
            
    def inorder(self, node):
        if node != None:
            if node.get_left():
                self.inorder(node.get_left())
            print(str(node.get_key()),' ', end='')
            if node.get_right():
                self.inorder(node.get_right())

    def postorder(self, node):
        if node != None:
            if node.get_left():
                self.postorder(node.get_left())
            if node.get_right():
                self.postorder(node.get_right())
            print(str(node.get_key()),' ', end='')

    def levelorder(self, root):
        q = queue()
        q.enqueue(root)
        while not q.is_empty():
            node = q.dequeue()
            print(str(node.get_key()),' ', end='')
            if node.get_left():
                q.enqueue(node.get_left())
            if node.get_right():
                q.enqueue(node.get_right())