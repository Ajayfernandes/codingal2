set1={1,2,3}
set2={4,5,7}
total = list(zip(set1,set2))
print(total)

list1 = [1,3,5,7]
list2 = [1,2,3,4]
together = list(zip(list1,list2[::-1]))
for x,y in together:
    print(x, "&", y)