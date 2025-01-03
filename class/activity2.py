class Vehicle:
    def __init__(self,maxspeed, mileage):
        self.ms = maxspeed
        self.mileage = mileage

modelx = Vehicle(250, 80)
print("maxspeed of model: ", modelx.ms)
print("the mileage of model: ", modelx.mileage)
