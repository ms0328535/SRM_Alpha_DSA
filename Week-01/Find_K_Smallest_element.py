def find_k_smallest(arr, k):
    n = len(arr)
    # We only need to find the first k minimum elements
    for i in range(min(k, n)):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the minimum element into place
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    # Return the first k elements manually collected
    result = []
    for i in range(min(k, n)):
        result.append(arr[i])
    return result

# Example Usage:
print(find_k_smallest([7, 10, 4, 3, 20, 15], 3)) 
# Output: [3, 4, 7]
