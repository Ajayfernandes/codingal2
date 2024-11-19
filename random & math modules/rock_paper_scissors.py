import random
choices = ['rock', 'paper', 'scissors']
c = int(input("How many times do you want to play? : "))
games = 0
while True:
    if games == c:
        break
    choice = input("rock,paper or scissors? :")
    computer_choice = random.choice(choices)

    if computer_choice == choice:
        print("It is a DRAW. Both you and the computer has chosen", choice)
        games+=1
    elif computer_choice == 'paper' and choice == 'scissors':
        print("You WIN as computer used paper")
        games+=1
    elif computer_choice == 'rock' and choice == 'scissors':
        print("computer WINS as computer used rock")
        games+=1
    elif computer_choice == 'paper' and choice == 'rock':
        print("computer WiNS as computer used paper")
        games+=1
    elif choice == 'paper' and computer_choice == 'scissors':
        print("computer WINs as compuer used scissors")
        games+=1
    elif choice == 'paper' and computer_choice == 'rock':
        print("You WIN as computer used rock")
        games+=1
    elif choice == 'rock' and computer_choice == 'scissors':
        print("You WIN as computer used scissors")
        games+=1
    else:
        print("please enter Rock,Paper or scissors")
    