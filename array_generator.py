import random

def generate_random_array(size):
    return [random.randint(1, 100000) for _ in range(size)]

import time

def measure_time(sort_function, arr):
    start = time.perf_counter()
    sort_function(arr)
    end = time.perf_counter()

    return (end - start) * 1000  