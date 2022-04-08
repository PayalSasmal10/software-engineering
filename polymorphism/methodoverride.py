# same method same parameter
class A:
    def div(self,a,b): # method overriden class
        print("I am in first method",a,b)

class B(A):
    def div(self,a,b): #method overriding class
        print("I am in 2nd method", a,b)


c = B()
c.div(30,20)