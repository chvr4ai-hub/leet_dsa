
# Time Complexity: O(n^2) - Although there is only one explicit loop, 'diff in nums' and 'nums.index(diff)' both perform linear searches (O(n)) on the list.
# Space Complexity: O(1) - No additional data structures that scale with input size are used.
nums = [2,7,11,15]
target = 26
pair = None

for i, n in enumerate(nums):
    diff = target - n
    if diff in nums:
        pair = (i, nums.index(diff))

if pair:
    print("Output: ", pair)
else:
    print("No pair found")
    