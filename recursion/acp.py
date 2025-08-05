def sum(x):
    if x <= 0:
        return 0
    return (x + sum(x -1))
x = int(input("enter a positive number: "))
if x < 0:
    print("Invalid input")
else:
    print(sum(x))