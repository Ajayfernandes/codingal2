weather = (1,0,1,0,0,1,0)
sunny = 0
rainy = 0
for i in range(0,7):
    if i == 1:
        rainy += 1
    if i == 0:
        sunny += 1
    
if rainy>sunny:
    print("it is rainy")
else:
    print("its sunny")
