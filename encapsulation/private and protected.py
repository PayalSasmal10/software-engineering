class Base:
    def __init__(self) -> None:
        self._a = 3
        self.__c = 4

class Derive:
    def __init__(self) -> None:
        Base.__init__(self)
        print("calling protected member ", self._a)
        print("calling private member ", self.__c)

d = Derive()
