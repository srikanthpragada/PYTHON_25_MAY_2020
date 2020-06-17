from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def process(self):
        pass


class B(A):
    # Override abstract method process()
    def process(self):
        print("Process in B")


# obj = A()
obj = B()
obj.process()
