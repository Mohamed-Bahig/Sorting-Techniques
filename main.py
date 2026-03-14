import csv

from array_generator import generate_random_array
from array_generator import measure_time

from Bubble_Sort.bubble_sort import bubble_sort
from Selection_Sort.selection_sort import selection_sort
from Insertion_Sort.insertion_sort import insertion_sort
from heap_sort.heap_sort import heap_sort
from quick_sort.quick_sort import sort as quick_sort
from merge_sort.merge_sort import sort as merge_sort


array_sizes = [1000, 5000, 10000]

results = []

for size in array_sizes:

    arr = generate_random_array(size)

    bubble_time = measure_time(bubble_sort, arr.copy())
    selection_time = measure_time(selection_sort, arr.copy())
    insertion_time = measure_time(insertion_sort, arr.copy())
    heap_time = measure_time(heap_sort, arr.copy())
    quick_time = measure_time(quick_sort, arr.copy())
    merge_time = measure_time(merge_sort, arr.copy())

    print(f"\nArray Size: {size}")
    print(f"Bubble Sort: {bubble_time:.2f} ms")
    print(f"Selection Sort: {selection_time:.2f} ms")
    print(f"Insertion Sort: {insertion_time:.2f} ms")
    print(f"Heap Sort: {heap_time:.2f} ms")
    print(f"Quick Sort: {quick_time:.2f} ms")
    print(f"Merge Sort: {merge_time:.2f} ms")

    results.append([size, bubble_time, selection_time, insertion_time, heap_time, quick_time, merge_time])


with open("results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Array Size",
        "Bubble Sort",
        "Selection Sort",
        "Insertion Sort",
        "Heap Sort",
        "Quick Sort",
        "Merge Sort"
    ])

    writer.writerows(results)

print("\nResults saved to results.csv")