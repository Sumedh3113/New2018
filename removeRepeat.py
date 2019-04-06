#removed issue of last element removal using prev pointer
class Element:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        
        data = input("Add an element:")
        node = Element(data)
        node.data = data
        node.next = self.head
        self.head = node

    def print(self):
        print_list = self.head
        while print_list:
            print(print_list.data)
            print_list = print_list.next
            
    def removerepeat(self):
        present = set()
        cur =  self.head
        prev = None
        while cur.next:
            if cur.data in present:
                cur.data = cur.ne00xt.data
                cur.next = cur.next.next
            else:
                present.add(cur.data)
                #print(cur.data)
                prev = cur
                cur = cur.next
        if cur.data in present:            
            prev.next = None
        print(present)          
        return self.head

ll = LinkedList()

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll.insert(e1)
ll.insert(e2)
ll.insert(e3)
        
ll.removerepeat()

ll.print()