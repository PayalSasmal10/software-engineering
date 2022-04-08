class Mother:
    motherName = ""
    def mother(self):
        print(self.motherName)

class Father:
    fatherName = ""
    def father(self):
        print(self.fatherName)

class Child(Mother,Father):
    def parents(self):
        print("Father :", self.motherName)
        print("Father :", self.fatherName)


c = Child()
c.father = "Achintya"
c.mother = "Sonali"

c.father()