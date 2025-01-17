import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return math.pi * self.radius * 2
    def give(self):
        print("the area of the circle is: ", self.area())
        print("the perimeter of the circle is", self.perimeter())
radius = float(input("what is the circles radius: "))
obj = Circle(radius)
obj.give()
