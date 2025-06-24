def xor(arr):
    res = 0 
    for i in arr:
        res = res^i
    return res

arr = []
a = int(input("How many values do u want to enter?"))
for i in range(a):
    b = int(input("enter a number: "))
    arr.append(b)

print("odd occurring number is", xor(arr))