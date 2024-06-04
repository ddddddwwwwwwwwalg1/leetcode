def func1(sort_arrays, target):
    left = 0
    right = len(sort_arrays) - 1
    while left <= right:
        mid = (left + right) // 2
        if target < sort_arrays[mid]:
            right = mid - 1
        elif target > sort_arrays[mid]:
            left = mid + 1
        else:
            return mid
    return -1


print(func1([1, 2, 3, 4, 5, 6], 5))
