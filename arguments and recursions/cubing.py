def cubing(x):
    x = x**3
    return x

def check(x):
    if x % 3 == 0:
        return cubing(x) 
    else: 
        return False
    
num = int(input("Enter a number: "))
print(check(num))
    
