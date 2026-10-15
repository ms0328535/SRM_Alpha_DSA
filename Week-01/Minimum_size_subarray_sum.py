def min_subarray_len(target, nums):
    left = 0
    current_sum = 0
    min_length = float("inf")
 
    for right in range(len(nums)):
        current_sum += nums[right]
 
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
 
    return 0 if min_length == float("inf") else min_length
 
 
if __name__ == "__main__":
    print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))   # Expected: 2  ([4, 3])
    print(min_subarray_len(4, [1, 4, 4]))            # Expected: 1
    print(min_subarray_len(11, [1, 1, 1, 1, 1, 1]))  # Expected: 0
 
