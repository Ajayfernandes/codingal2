class Myclass:
    __privateVar = 2
    def __privMeth(self):
        print("my class")
    def hello(self):
        print(Myclass.__privateVar)
obj = Myclass()
obj.hello()
obj.__privMeth() # this will generate an error as a private method cannot be directly accessed from
                 #outside the class
