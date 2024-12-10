a = {'helo':2, 'halo':2, 'hello':3, 'hallo':2}
number = 2
frequency = 0
for keys in a:
        if a[keys] == number:
            frequency += 1

print("the number 2 occurs", frequency , "times in the dictionary")
