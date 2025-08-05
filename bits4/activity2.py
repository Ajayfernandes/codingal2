def checkpower4(n):
    count  =0
    if (n & (~((n-1) & n))):
        while n>1:
            n>>=1
            count +=1
        if count % 2 == 0:
            print("n is a power of 4")
        else:
            print({n}, "is not a power of 4")
n = int(input("enter a number: "))
checkpower4(n)

