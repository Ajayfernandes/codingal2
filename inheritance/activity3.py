class Bird:
    def __init__(self):
        print("bird is ready")
    def type(self):
        print("bird")
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("penguin is ready")
    def bird_type(self):
        print("penguin")
obj = Penguin()
obj.type()
obj.bird_type()
