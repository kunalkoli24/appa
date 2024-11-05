import threading
import time

# Function to merge two halves
def merge(arr, left_half, right_half):
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

# Single-threaded Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)  # Recursive call on left half
        merge_sort(right_half)  # Recursive call on right half

        merge(arr, left_half, right_half)


# Multithreaded Merge Sort
def multithreaded_merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Creating threads for sorting the halves
        left_thread = threading.Thread(target=multithreaded_merge_sort, args=(left_half,))
        right_thread = threading.Thread(target=multithreaded_merge_sort, args=(right_half,))

        left_thread.start()
        right_thread.start()

        left_thread.join()
        right_thread.join()

        merge(arr, left_half, right_half)

# Function to measure execution time
def measure_time(func, arr):
    start_time = time.time()
    func(arr)
    return time.time() - start_time

# Main function to satisfy project objectives
if __name__ == "__main__":
    array_size = 10000  # You can change this value to test with different input sizes
    
    # Best case: Sorted array
    arr_best = list(range(array_size))  # Already sorted array
    arr_best_copy = arr_best.copy()

    # Worst case: Reverse sorted array
    arr_worst = list(range(array_size, 0, -1))  # Reversed array
    arr_worst_copy = arr_worst.copy()

    # Time for Single-threaded Merge Sort (Best Case)
    print("Running single-threaded merge sort for best case...")
    time_single_best = measure_time(merge_sort, arr_best)
    print(f"Time (Best Case - Single-threaded): {time_single_best:.5f} seconds")

    # Time for Multithreaded Merge Sort (Best Case)
    print("Running multithreaded merge sort for best case...")
    time_multi_best = measure_time(multithreaded_merge_sort, arr_best_copy)
    print(f"Time (Best Case - Multithreaded): {time_multi_best:.5f} seconds")

    # Time for Single-threaded Merge Sort (Worst Case)
    print("Running single-threaded merge sort for worst case...")
    time_single_worst = measure_time(merge_sort, arr_worst)
    print(f"Time (Worst Case - Single-threaded): {time_single_worst:.5f} seconds")

    # Time for Multithreaded Merge Sort (Worst Case)
    print("Running multithreaded merge sort for worst case...")
    time_multi_worst = measure_time(multithreaded_merge_sort, arr_worst_copy)
    print(f"Time (Worst Case - Multithreaded): {time_multi_worst:.5f} seconds")
