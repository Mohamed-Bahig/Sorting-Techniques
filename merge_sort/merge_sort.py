def merge(arr, left, mid, right):
    left_subarray = arr[left:mid + 1]
    right_subarray = arr[mid + 1:right + 1]

    i, j, k = 0, 0, left
    while i < len(left_subarray) and j < len(right_subarray):
        if left_subarray[i] <= right_subarray[j]:
            arr[k] = left_subarray[i]
            i += 1
        else:
            arr[k] = right_subarray[j]
            j += 1
        k += 1

    while i < len(left_subarray):
        arr[k] = left_subarray[i]
        i += 1
        k += 1

    while j < len(right_subarray):
        arr[k] = right_subarray[j]
        j += 1
        k += 1
