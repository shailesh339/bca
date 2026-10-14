def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    pivot = arr[mid]

    left = []
    equal = []
    right = []

    for i in arr:
        if i == pivot:
            equal.append(i)
        elif i < pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + equal + quick_sort(right)


arr = list(map(int, input("Enter numbers separated by spaces to sort: ").split()))
print("Sorted array:", quick_sort(arr))