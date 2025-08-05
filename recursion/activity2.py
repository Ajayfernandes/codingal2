def factorial(x):
    if x == 0 or x == 1:
        return 1
    return (x* factorial(x - 1))
x = int(input("enter a number: "))
if x < 0:
    print("factorials dont exist for negative numbers")
else:
    print(factorial(x))
