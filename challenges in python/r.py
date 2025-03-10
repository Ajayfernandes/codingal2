class Flashcards:
    def __init__(self):
        # Initialize an empty dictionary to store flashcards
        self.flashcard = {}
    
    def add_flashcard(self):
        while True:
            # Take input for the word and its meaning
            word = input("What is the word? ")
            meaning = input("What is the meaning of the word? ")
            
            # Add the word and meaning to the dictionary
            self.flashcard[word] = meaning
            
            # Ask if the user wants to add more flashcards
            check = input("Do you want to add more words and their meanings? (yes/no): ").lower()
            if check != "yes":
                break
        
        # Print the final flashcard dictionary
        print("\nHere are the flashcards you added:")
        for word, meaning in self.flashcard.items():
            print(f"{word}: {meaning}")


# Create an instance of the Flashcards class and call the add_flashcard method
obj = Flashcards()
obj.add_flashcard()