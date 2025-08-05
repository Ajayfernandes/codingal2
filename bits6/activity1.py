import math
def print_power_set(set,setsize):
    Power_Set_Size = int(math.pow(2,setsize))
    outer = 0 
    inner = 0
    for outer in range(0, Power_Set_Size):
        for inner in range(0,setsize):
            if (outer & (1<< inner)) > 0:
                print(set[inner],end = "")
        print("")
size = int(input("enter array size: "))
set = []
for i in range(0,size):
    n = int(input("Enter Element: "))
    set.append(n)

print_power_set(set, len(set))
