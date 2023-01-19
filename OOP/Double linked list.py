class Node:
    
    
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None
        
class DoubleLinkedList:
    
    
    def __init__(self):
        self.head = None
        
    def public(self):
        node = self.head
        while node.next:
            print(node.value.value, end=', ')
            node = node.next
        print(node.value.value)
        
    def getElem(self, pos):
        node = self.head
        i = 0
        while node.next:
            if i == pos:
                print(f'Элемент под индексом {pos} - {node.value.value}')
                break
            else:
                node = node.next
                i += 1
    
    def getLen(self):
        if self.head is None:
            print("Список пуст")
        else:
            i = 0
            node = self.head
            while node:
                node = node.next
                i += 1
        return i
        
    def addToEnd(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
            new_node.prev = last
            last = new_node
        
    def insert(self, value, pos):
        new_node = Node(value)
        i = 0
        if pos == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif pos < 0 or pos > self.getLen():
              print('Значение вставки меньше нуля или превышает размер списка')
        else:
            node = self.head
            while i < pos:
                node = node.next
                i += 1
            new_node.next = node
            node.prev.next = new_node
            new_node.prev = node.prev
            node.prev = new_node
            
    def removeElem(self, pos):
        remNode = self.head
        i = 0
        if pos < 0 or pos > self.getLen():
              print('Значение удаления меньше нуля или превышает размер списка')
        elif pos == 0:
            remNode.next.prev = None
            self.head = remNode.next  
        elif pos == self.getLen():
            while remNode.next:
                remNode = remNode.next
            remNode.prev.next = None
        else:
            while i < pos:
                remNode = remNode.next
                i += 1
            remNode.prev.next = remNode.next
            remNode.next.prev = remNode.prev
                  
dll = DoubleLinkedList()
a = Node(7)
b = Node(12)
c = Node(88)
d = Node(59)
e = Node(111)
dll.addToEnd(a)
dll.addToEnd(b)
dll.addToEnd(c)
dll.addToEnd(e)
print(dll.getLen())
dll.getElem(0)
dll.public()
dll.removeElem(-1)
dll.public()
dll.removeElem(12)
dll.public()
dll.removeElem(4)
dll.public()