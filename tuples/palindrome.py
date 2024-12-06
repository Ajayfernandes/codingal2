palindrome = (1,2,3,2,1)
q = len(palindrome) - 1
z = 0
c = 0
while q>=z:
    if palindrome[q] != palindrome[z]:
        print("this is not a palindrome")
        c=1
        break
    else:
        z += 1
        q -= 1

if c==0:
    print("It is a palindrome")

