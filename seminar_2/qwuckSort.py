from random import randint


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)

array = [randint(0, 10) for i in range(10)]
print(array)
print(quick_sort(array))