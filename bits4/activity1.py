def checkpower2(number):
    if number <= 0:
        return False
    return (number & (number-1)) == 0
number = int(input("enter a number:"))
if checkpower2(number):
    print("the number is a power of 2")
else:
    print("the number is not a power of 2")