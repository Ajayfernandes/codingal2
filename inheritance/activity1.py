class Vehicle:
    def __init__(self,name,maximum_speed,milage):
        self.name = name
        self.maximum_speed = maximum_speed
        self.milage = milage

class Bus(Vehicle):
        pass

obj = Bus("car", 240, 25)
print("the name of the vehicle is", obj.name)
print("the maximum speed is", obj.maximum_speed)
print("the milage of the vehicle is", obj.milage)