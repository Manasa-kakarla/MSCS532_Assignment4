def heapsort(arr):
    n = len(arr)

    # Build a max-heap
    def heapify(arr, n, i):
        largest = i        # Initialize largest as root
        left = 2 * i + 1   # Left child index
        right = 2 * i + 2  # Right child index

        # Check if left child exists and is greater than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if right child exists and is greater than largest so far
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If largest is not root, swap and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap
            heapify(arr, n, largest)  # Recursively heapify the affected subtree

    # Step 1: Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[i], arr[0] = arr[0], arr[i]
        # Call heapify on the reduced heap
        heapify(arr, i, 0)

    return arr

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heapsort(arr)
print("Sorted array is:", sorted_arr)
