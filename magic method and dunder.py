from os import name


class Person:
    def __init__(self, name,age) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"value of obj: {self.name, self.age}"

    def __add__(self,other):
        return other+self.name

    def __del__(self):
        print("Object is being deleted")


p = Person("Payal", 27)
print(p+"Hello")
del p