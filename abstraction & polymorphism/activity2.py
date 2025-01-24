from abc import ABC, abstractmethod
class Animals(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animals):
    def move(self):
        print("i can run and walk")
class Bird(Animals):
    def move(self):
        print("i can fly")
class Fish(Animals):
    def move(self):
        print("i can swim")
obj = Human()
obj2 = Bird()
obj3 = Fish()
obj.move()
obj2.move()
obj3.move()
