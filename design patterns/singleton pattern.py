# when we want to create single instance then we should use singleton design pattern
from abc import  ABCMeta, abstractclassmethod
class Domain(metaclass=ABCMeta):
    @abstractclassmethod
    def print_data():
        """"Implementation is in childwise"""

class DomainName(Domain):
    __intance = None

    def __init__(self, name) -> None:
        if DomainName.__intance != None:
            raise Exception("We can't create obj as this is a singleton method")
        else:
            self.name = name
            DomainName.__intance = self
    @staticmethod
    def get_instance():
        if DomainName.__intance == None:
            DomainName("Default name")
        return DomainName.__intance
    
    @staticmethod
    def print_data():
        print(f"Name:{DomainName.__intance.name}")


d = DomainName("payalsasmal.com")
print(d)
d.print_data()

d1 = DomainName.get_instance()
print(d1)
d1.print_data()


