from hashlib import new


class Node:
    def __init__(self, data) -> None:
        self.head = None
        self.next = None
        self.data = data

class linkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert(self,data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode

        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def add_back(self,data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            temp = self.head
            newNode = Node(data)
            while(temp):
                if temp.next == None:
                    newNode = Node(data)
                    temp.next = newNode
                    #temp = newNode
                    break
                else:
                    temp = temp.next



    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, "->", end="")
            temp = temp.next
        print("end")


lin = linkedList()
lin.insert(3)
lin.insert(8)
lin.add_back(4)
lin.add_back(5)
lin.insert(1)
lin.insert(10)
lin.printList()