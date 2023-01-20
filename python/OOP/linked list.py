class Node:
    
        
    def __init__(self, value):
        self.value = value
        self.next = None

            
class LinkedList:
    
    
    def __init__(self):
        self.head = None
    
    def addToEnd(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node 
        else:
            islast = self.head
            while islast.next:
                islast = islast.next
            islast.next = new_node
            
    def insert(self, value, pos):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node 
            print('Списк был пуст. Элемент добавлен в начало')
        elif pos == 0:
            new_node.next = self.head
            self.head = new_node 
        elif self.head is not None:
            i = 1
            prev = self.head          
            while prev.next:       
                if i == pos:                
                    new_node.next = prev.next
                    prev.next = new_node    
                    break
                i += 1
                prev = prev.next     
            else:
                self.addToEnd(value)
            
    def public(self):
        islast = self.head
        while islast.next:
            print(islast.value.value, end=", ")
            islast = islast.next
        print(islast.value.value)
        
    def checkElem(self, value):
        islast = self.head.value
        i = 0
        while islast:
            if value == islast:
                print(f'Элемент {value.value} имеет индекс {i}')
                break
            else:
                islast = islast.next
                i += 1
                
    def removeElem(self, pos):
        node = self.head
        if pos == 0:
            self.head = node.next
            node = None
        else:
            i = 1
            while node.next:
                prev_node = node
                node = node.next
                if pos == i:
                    prev_node.next = node.next
                    node = None
                    break
                else:
                    i += 1
                    prev_node = node.next
            

a = Node(12)
b = Node(56)
c = Node(87)
d = Node(109)
e = Node(333)
g = Node(333)
ll = LinkedList()
ll.addToEnd(a)
ll.addToEnd(b)
ll.addToEnd(c)
ll.addToEnd(d)
print('список')
ll.public()
ll.insert(e, 7)
print('после вставки')
ll.public()
ll.removeElem(2)
print('после удаления')
ll.public()
ll.checkElem(a)