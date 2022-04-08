class Parent:
    def func1(self):
        print("I am in func1")

class child(Parent):
    def func2(self):
        print("I am in func2")

obj = child()
obj.func2()
