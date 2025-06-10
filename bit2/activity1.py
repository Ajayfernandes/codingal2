def numberofbits(n):
    a = 0
    b = 0
    while n:
        if n & 1 == 1:
            a += 1
        else:
            b += 1
        n >>= 1
    print("number of zeros is ", b )
    print("number of ones is ", a )
x = int(input("enter a number: "))
numberofbits(x)