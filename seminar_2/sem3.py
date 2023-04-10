from random import randint


def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while (temp < array[j] and j >= 0):
            array[j + 1] = array[j]
            j -= 1
            array[j + 1] = temp

array = [randint(0, 10) for i in range(10)]
print(array)
insertion_sort(array)
print(array)