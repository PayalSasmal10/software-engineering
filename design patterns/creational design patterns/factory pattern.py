from abc import ABCMeta, abstractmethod

class AbstractClass(metaclass=ABCMeta):
    @abstractmethod
    def person_method(self):
        """This is an abstract method"""

class Student(AbstractClass):
    def __init__(self) -> None:
        self.name = "Basic teacher name"
    
    def person_method(self):
        print("I am student")

class Teacher:
    def __init__(self) -> None:
        self.name = "Basic teacher name"

    def person_method(self):
        print("I am a Teacher")


class FactoryClass:
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        else:
            raise Exception("This type of person not available")


if __name__ == "__main__":
    choice = input("what type of person do you want to create?\n")
    person = FactoryClass.build_person(choice)
    person.person_method()
    


