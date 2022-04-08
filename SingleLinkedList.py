class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data

class Linkedlist:
    def __init__(self) -> None:
        self.head = None

    def add_front(self,data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node

        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def add_back(self,data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            
            temp =  self.head
            while(temp):
                if temp.next == None:
                    new_node = Node(data)
                    temp.next = new_node
                    temp = new_node
                    return
                        
                else:
                    temp = temp.next

    def delete(self,data):
        temp = self.head
        if temp != None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return 
        
        while(temp is not None):
            if temp.data == data:
                break
            prv = temp
            temp = temp.next


    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, "->", end="")
            temp = temp.next
        print("end")


s = Linkedlist()
s.add_front(3)
s.add_back(5)
s.add_back(6)
s.add_front(2)
s.add_front(8)
s.add_front(9)
s.printList()
s.delete(8)
s.printList()
                



