x = int(input("enter a number: "))
y = int(input("enter position to check"))
def bitssetornot(x, y):
    mask = 1
    if y & mask == 1 or y & mask == 0:
        if x & (1<<(y-1)):
            print("set")
        else:
            print("not set")
bitssetornot(x,y)

        


    