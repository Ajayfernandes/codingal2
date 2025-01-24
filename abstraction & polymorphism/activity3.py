class India:
    def capital(self):
        print("New Dehli is the capital of india")
    def language(self):
        print("the most common language used is hindi")
    def type(self):
        print("India is a deleloping country")

class Germany:
    def capital(self):
        print("Berlin is the capital of Germany")
    def language(self):
        print("the most common language used is German")
    def type(self):
        print("India is a deleloped country")
obj_india = India()
obj_germany = Germany()
for i in (obj_india,obj_germany):
    i.capital()
    i.language()
    i.type()

