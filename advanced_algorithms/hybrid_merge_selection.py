from..merge_sort.merge_sort import merge
from..Insertion_Sort.insertion_sort import insertion_sort

def hybrid_merge_sort(arr, left, right, threshold):
    if right - left + 1 <= threshold:
        insertion_sort(arr, left, right)
        return

    if left < right:
        mid = left + (right - left) // 2
        hybrid_merge_sort(arr, left, mid, threshold)
        hybrid_merge_sort(arr, mid + 1, right, threshold)
        merge(arr, left, mid, right)