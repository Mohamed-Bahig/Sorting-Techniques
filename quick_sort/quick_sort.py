import random

def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)

        quick_sort(arr, pivot_index + 1, high)


def sort(arr):
    quick_sort(arr, 0, len(arr) - 1)
    return arr