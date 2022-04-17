class Node:
    def __init__(self,data) -> None:
        self.next = None
        self.data = data

class reverseLinkedList:
    def __init__(self) -> None:
        self.head = None

    def add_front(self,data):
        if self.head  == None:
            newNode   = Node(data)
            self.head = newNode

        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def add_back(self,data):
        if self.head == None:
            newNode  =  Node(data)
            self.head = newNode

        else:
            temp = self.head
            while(temp):
                if temp.next  == None:
                    newNode   = Node(data)
                    temp.next = newNode
                    break
                else:
                    temp = temp.next

    def reverseList(self):
        current = self.head
        prev = None
        while(current != None):
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        self.head = prev

    
    def printAll(self):
        temp = self.head
        while(temp):
            print(temp.data, "->", end=" ")
            temp = temp.next

        print("end")


r = reverseLinkedList()
r.add_front(4)
r.add_front(6)
r.add_front(1)
r.add_front(65)
r.add_back(65)
r.add_back(65)
r.printAll()
r.reverseList()
r.printAll()
