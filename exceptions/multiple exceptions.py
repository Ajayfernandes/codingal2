try:
    a,b = eval(input("enter 2 numbers with a coma inbetween"))
    c = a/b
    print("the result is", c)
except ZeroDivisionError as ex:
    print("exception:" , ex)
except SyntaxError as f:
    print("exception: ", f)
except:
    print("invalid input")
else:
    print("no exception occured")
finally:
    print("This will get executed regardless of the above operations")
