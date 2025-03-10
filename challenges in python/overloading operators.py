class A:
    def __init__(self, a):
        self.a = a
    def __lt__(self,other):

        if self.a < other.a:
            return "first value is less than the second value"
        else:
            return "first value is not less than the second value"
    def __eq__(self,other):
        if self.a == other.a:
            return "both the values are equal"
        else:
            return "both values are not equal"
obj = A(5)
obj2 = A(4)
print("Current values are: ",obj.a, obj2.a)
print(obj<obj2)

obj3 = A(17)
obj4 = A(17)
print("the current values are", obj3.a,obj4.a)
print(obj3 == obj4)
        

    