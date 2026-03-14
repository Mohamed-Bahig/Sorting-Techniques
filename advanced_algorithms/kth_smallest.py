
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


def kth_smallest(arr, low, high, k):
    if low <= high:

        pivot_index = partition(arr, low, high)

        if pivot_index == k:
            return arr[pivot_index]

        elif pivot_index > k:
            return kth_smallest(arr, low, pivot_index - 1, k)

        else:
            return kth_smallest(arr, pivot_index + 1, high, k)


def find_kth_smallest(arr, k):
    return kth_smallest(arr, 0, len(arr) - 1, k - 1)


if __name__ == "__main__":
    arr = [3, 41, 16, 25, 63, 52, 40]
    k = 3

    result = find_kth_smallest(arr, k)

    print(f"{k}th smallest element is:", result)
