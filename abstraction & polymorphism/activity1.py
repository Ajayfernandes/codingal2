from abc import ABC , abstractmethod
class abstract(ABC):
    def give(self,x):
        print(x)

    @abstractmethod
    def hello(self):
        pass
class sub_class(abstract):
    def hello(self):
        print("implemented abstract method")
obj = sub_class()
obj.hello()
obj.give(10)
