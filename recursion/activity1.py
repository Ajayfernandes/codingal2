def print1to10(x):
    if x > 10:
        return
    print(x)
    print1to10(x+1)
print1to10(1)
    