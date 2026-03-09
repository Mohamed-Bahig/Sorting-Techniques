import random
import time


# Selection Sort Algorithm
def selection_sort(array):
    ln = len(array)

    for i in range(ln - 1):
        minIndx = i

        # Find the smallest element in the remaining array
        for j in range(i + 1, ln):
            if array[j] < array[minIndx]:
                minIndx = j

        # Swap the found minimum with the first unsorted element
        array[i], array[minIndx] = array[minIndx], array[i]

    return array


# -------- Generate Random Array --------
# Recommended sizes for O(n²) algorithms
# Example: 1000, 2500, 5000, 7500, 10000

siz = 10000
array = [random.randint(0, siz) for _ in range(siz)]


# -------- Measure Execution Time --------
startTime = time.perf_counter()

selection_sort(array)

endTime = time.perf_counter()

elapsedTime = endTime - startTime


# -------- Print Result --------
print(f"Selection Sort Execution Time: {elapsedTime:.4f} seconds, Size: {siz}")