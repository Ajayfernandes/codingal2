import random
a = int(random.randint(1,100))
c = 0
print("you only have 7 tries to guesss the right number")
while True:
    guess = int(input("what number would you like to guess?(1 to 100) : "))
    if guess == a:
        print("congrats! You guessed the right number")
        break
    elif abs(a - guess) >= 50:
        c += 1
        print("you are very far from the number")
    elif abs(guess - a) >= 50:
        c += 1
        print("you are very far from the number")
    elif abs(a - guess) <= 25:
        c += 1
        print("you are getting close")
        print("your guess is lower than the number")
    elif abs(guess - a) >= 25:
        c += 1
        print("you are getting close")
        print("your guess is higher than the number")
    if c > 7:
        print("you have used up all your chances. You LOSE.")
        print("the number was", a)
        break

