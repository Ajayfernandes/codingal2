x = int(input("Enter a number: "))

def find_rightmost_set_bit(x):
    if x == 0:
        print("No set bits (number is zero).")
        return 
     
    rightmost_set_bit = x & -x

    position = 1
    number = 1
    while not (rightmost_set_bit & number):
        number <<= 1
        position += 1

    print(f"Rightmost set bit is at position {position}")

find_rightmost_set_bit(x)