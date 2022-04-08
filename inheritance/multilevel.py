class GFather:
    def __init__(self,grandfatherName) -> None:
        self.grandfatherName = grandfatherName

class Father(GFather):
    def __init__(self,fatherName, grandfatherName) -> None:
        self.fatherName = fatherName

        GFather.__init__(self, grandfatherName)


class Child(Father):
    def __init__(self, childName, fatherName, grandfatherName) -> None:
        self.childName = childName

        super().__init__(self,fatherName, grandfatherName)

    def printAll(self):
        print("GrandFather name: ", self.grandfatherName)
        print("Father name: ", self.fatherName)
        print("childName name: ", self.childName)


c = Child("Payal", "Achintya", "Gopal")
print(c.grandfatherName)
c.printAll()


