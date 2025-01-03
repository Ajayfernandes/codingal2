class IOstring:
    def __init__(self):
        self.str1 = ""
    
    def word(self):
        self.str1 = input('write a word: y ')

    def give(self):
        print(self.str1.upper())

obj = IOstring()
obj.word()
obj.give()

