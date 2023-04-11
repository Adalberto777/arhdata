from random import randint


def heapify(array, heapSize, rootIndex):
    largest = rootIndex
    leftChild = 2 * rootIndex +1
    rightChild = 2 * rootIndex +2

    if (leftChild < heapSize and array[leftChild] > array[largest]):
        largest = leftChild

    if (rightChild < heapSize and array[rightChild] > array[largest]):
        largest = rightChild

    if (largest != rootIndex):
        temp = array[rootIndex]
        array[rootIndex] = array[largest]
        array[largest] = temp
        heapify(array, heapSize, largest)

def heapSort(array):
    for i in range(len(array)//2 -1, 0, -1):    
        heapify(array, len(array), i)

    for i in range(len(array) -1, 0, -1):
        temp = array[0]
        array[0] = array[i]
        array[i] = temp

        heapify(array, i, 0)

array = [randint(0, 10) for i in range(10)]
print(array)
heapSort(array)
print(array)