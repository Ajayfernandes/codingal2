def numberofbits(n):
    count = 0
    while n:
        count += 1
        n >>= 1
    return count
a = int(input("enter a number: "))
print(numberofbits(a))

