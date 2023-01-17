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

        # else:
        #     self.addToEnd(value)
            
       
    def public(self):
        islast = self.head
        pub = []
        while islast.next:
            pub.append(islast.value.value)
            islast = islast.next
        pub.append(islast.value.value)
        print(pub)
        
    def checkElem(self, value):
        islast = self.head
        i = 0
        while islast.value:
            if islast.value.value == value.value:
                print(f"Значение {value.value} содержится под индексом {i}")
                break
            else:  
                i += 1
                islast = islast.next
        else:
            print(f"Значение {value.value} отсутствует в списке")
            
    def removeElem(self, value):
        pass
            

a = Node(12)
b = Node(56)
c = Node(87)
d = Node(109)
e = Node(333)
ll = LinkedList()
ll.addToEnd(a)
ll.addToEnd(b)
ll.addToEnd(c)
ll.addToEnd(d)
ll.insert(e, 7)
ll.public()
ll.checkElem(e)