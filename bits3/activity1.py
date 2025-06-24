def check(num1, num2):
    if num1 ^ num2 == 0:
        print("number is even")
    else:
        print("number is odd")

num1 = int(input("enter a number"))
num2 = int(input("enter a number"))

check(num1, num2)
