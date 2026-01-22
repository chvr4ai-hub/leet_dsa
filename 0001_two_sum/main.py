# Raw Method 
nums = [2,7,11,15]
target = 9
pair = None
# Time Complexity: O(n^2) - The nested loops result in roughly n²/2 comparisons in the worst case.
# Space Complexity: O(1) - No additional data structures are used that scale with the input size.
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            pair = (i, j)
            break
    if pair:
        break