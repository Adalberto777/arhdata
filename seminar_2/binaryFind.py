def binary(array, k):
    first = 0
    last = len(array) - 1
    while(first <= last):
        mid = (first + last) // 2
        if array[mid] == k:
            return True
        else:
            if k < array[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False

array = [1, 2, 3, 4, 5, 6, 7]
print(binary(array, 5))    