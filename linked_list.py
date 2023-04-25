class Node:
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, value) -> None:
        newNode = Node(value)
        self.head = newNode
        self.tail = None
        self.length = 1
    
    def insert_at_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = None
        else:
            self.tail = newNode    
            self.tail.next = None
            
        self.length += 1
        return self
    
    def remove_at_end(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def print(self):
        """ Utility function """
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)
