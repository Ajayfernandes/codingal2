class Flashcards:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
        self.flashcard = {}

    def add_flashcard(self):
        while True:
            self.word = input("what is the word?")
            self.meaning = input("what is the meaning of the word")
            self.flashcard[self.word] = self.meaning
            check = input("do you want to add more words and their meanings?(yes/no): ")
            if check.lower() == "no":
                print(self.flashcard)
                break
    
obj = Flashcards("word", "meaning")
obj.add_flashcard()