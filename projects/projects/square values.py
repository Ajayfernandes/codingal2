first_num = int(input("what is the starting number of the range of numbers? : "))
end_num = int(input("what is the ending number of the range of numbers? : "))
even = []
odd = []
while True:
    if first_num < end_num:
        a = first_num **2 
        if a % 2 == 0:
            even.append(a)
            first_num += 1
        else:
            odd.append(a)
            first_num += 1
    else:
        break
print("the even numbers are", even)
print("the odd numbers are", odd)

