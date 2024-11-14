word = input("what word would you lke to key in: ")
c = 0
for letters in word:
    if letters == "A":
        c = c + 1
        break
if c > 0 :
    print("found 'A'") 
else: 
    print("'A' not found")

