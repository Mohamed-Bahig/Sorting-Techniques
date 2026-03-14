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


# Example: 1000, 2500, 5000, 7500, 10000

siz = 10000
array = [random.randint(0, siz) for _ in range(siz)]



startTime = time.perf_counter()

selection_sort(array)

endTime = time.perf_counter()

elapsedTime = endTime - startTime


print(f"Selection Sort Execution Time: {elapsedTime:.4f} seconds, Size: {siz}")
