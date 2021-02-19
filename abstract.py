from abc import ABCMeta, abstractmethod


class Calculation(metaclass=ABCMeta):

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def subtract(self):
        pass

    def multiply(self):
        pass

    def division(self):
        pass


class Calculator(Calculation):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)

    def subtract(self):
        print(self.a - self.b)


take = Calculator(10, 5)
take.add()
take.subtract()