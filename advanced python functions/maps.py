x = [1,2,3,4,5]
y = [5,4,3,2,1]

result = list(map(lambda a,b : a + b , x,y))
print(result)

def sq(n):
    return n*n
square = map(sq, x)
print(list(square))