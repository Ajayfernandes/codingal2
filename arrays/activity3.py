def max_value(a):
    b = len(a)
    if b == 1:
        return a[0]
    return max(a[0] , max_value(a[1:]))
def min_value(a):
    b = len(a)
    if b ==1:
        return a[0]
    return min(a[0], min_value(a[1:]))
arr = [23,1234,456,12,5678]
print(max_value(arr))
print(min_value(arr))