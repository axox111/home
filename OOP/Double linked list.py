class Node:
    
    
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None
        
class DoubleLinkedList:
    
    
    def __init__(self):
        self.head = None
        
    def addToEnd(self, value):
        new_node = self.head
        
        
dll = DoubleLinkedList()
a = Node(7)
b = Node(12)
c = Node(88)
d = Node(59)