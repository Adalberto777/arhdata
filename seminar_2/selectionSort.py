from random import randint


def selection_sort(array):
    for i in range(0, len(array) -1):
        temp_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[temp_index]:
                temp_index = j
            temp = array[i]
        array[i] = array [temp_index]   
        array[temp_index] = temp



array = [randint(0, 10) for i in range(10)]
print(array)
selection_sort(array)
print(array)