class Myclass:
    __privateVar = 2
    def __privMeth(self):
        print("my class")
    def hello(self):
        print(Myclass.__privateVar)
obj = Myclass()
obj.hello()
obj.__privMeth()
