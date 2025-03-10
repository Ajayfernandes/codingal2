import random
class Fruit_quiz:
    def __init__(self):
        self.fruits = {'banana':'yellow', 'grape':'purple','mango':'yellow'}
    def quiz(self):
        while True:
            
            self.question = random.choice(self.fruits.items(keys))
            self.question = self.question.lower()
            self.answer = input("what is the colour of",self.question,"? :")
            if self.answer == self.fruits(self.question.values()):
                print("your answer is correct!")
                break
            else:
                print("your answer is wrong. Try again")
obj = Fruit_quiz()
obj.quiz()