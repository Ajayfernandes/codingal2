class Computer:
    def __init__(self):
        self.__maxprice = 100
    def sell(self):
        print("the max selling price is", self.__maxprice)
    def setmaxprice(self, mp):
        self.__maxprice = mp
obj = Computer()
obj.sell()
obj.__maxprice = 150
obj.sell()
obj.setmaxprice(130)
obj.sell()