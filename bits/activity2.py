#oddeven using bitwise operators
def isEvenOdd(n):
    if n ^ 1 == n +1:
        return True
    else:
        return False
num = int(input("enter a number: "))
if isEvenOdd(num):
    print(num , "is even")
else:
    print(num , "is odd")