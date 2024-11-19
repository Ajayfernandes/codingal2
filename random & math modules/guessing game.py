import random
number = random.randint(0,15)
chances=0
while True:
    print("guess a number from 0 to 15")
    guess = int(input("What number would u like to choose? :"))
    chances +=1
    if guess == number:
        print("congrats! you have chosen the right number")
        break
    else:
        print("incorrect guess")
        if chances==5:
            print("You have exhausted your chances to guess the number.Correct number is:", number)