# Write a program for analysis of quick sort by using deterministic and randomized variant

import random
import time

# Deterministic Quick Sort
def quick_sort_deterministic(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # Choosing the first element as the pivot
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort_deterministic(left) + [pivot] + quick_sort_deterministic(right)

# Randomized Quick Sort
def quick_sort_randomized(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)  # Randomly choosing a pivot
    pivot = arr[pivot_index]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort_randomized(left) + [pivot] + quick_sort_randomized(right)

def main():
    # Input from user
    user_input = input("Enter numbers separated by spaces: ")
    arr = list(map(int, user_input.split()))

    # Analyzing deterministic Quick Sort
    start_time = time.time()
    sorted_deterministic = quick_sort_deterministic(arr)
    time_deterministic = time.time() - start_time
    print("Deterministic Quick Sort Result:", sorted_deterministic)
    print("Time taken (Deterministic): {:.6f} seconds".format(time_deterministic))

    # Analyzing randomized Quick Sort
    start_time = time.time()
    sorted_randomized = quick_sort_randomized(arr)
    time_randomized = time.time() - start_time
    print("Randomized Quick Sort Result:", sorted_randomized)
    print("Time taken (Randomized): {:.6f} seconds".format(time_randomized))

if __name__ == "__main__":
    main()
