import random
import time


def selection_sort(array):
    ln = len(array)

    for i in range(ln - 1):
        minIndx = i

  
        for j in range(i + 1, ln):
            if array[j] < array[minIndx]:
                minIndx = j

        array[i], array[minIndx] = array[minIndx], array[i]

    return array

