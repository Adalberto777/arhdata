from random import randint


def bubble_sort(array):
    for i in range(len(array) -1, 0, -1):
        flag = True
        for j in range(0, i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                flag = False
        if flag:
            return

array = [randint(0, 10) for i in range(10)]
print(array)
bubble_sort(array)
print(array)