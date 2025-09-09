def check_sorted(a):
    b = len(a)
    if b == 1 or b ==0:
        return True
    return a[0]<=a[1] and check_sorted(a[1:])
arr = [1,2,3,12,15]
if check_sorted(arr):
    print("The array is sorted")
else:
    print("The array is not sorted.")




