# same method diff parameters
class A:
    def div(self,a,b):
        print("I am in first method",a,b)

class B(A):
    def div(self,a,b,c):
        print("I am in 2nd method", a,b,c)


c = B()
c.div(30,20,30)