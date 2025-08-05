def swap_ab(a,b):
    a = a + b
    b = a-b
    a = a-b
    print("a is", a , "b is", b)

def swap_ab_xor(a,b):
    a = a^b
    b = a^b
    a = a^b
    print("a is", a, "b is", b)


swap_ab_xor(12,42)
swap_ab(13,56)

