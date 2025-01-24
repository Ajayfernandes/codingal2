class Point:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    def give(self):
        return "({},{})".format(self.x,self.y)
point1 = Point(2,3)
print(point1)

