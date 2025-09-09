def sum_array(a):
    b = len(a)
    if b == 1:
        return a[0]
    return (a[0] + sum_array(a[1:]))
arr = [1,5,10]
print(sum_array(arr))
