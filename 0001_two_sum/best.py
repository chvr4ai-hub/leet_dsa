# Using dict
# Time Complexity: O(n) - We iterate through the list once, and dictionary lookups/inserts are O(1) on average. 
# Space Complexity: O(n) - In the worst case, we store all n elements in the dictionary.
nums = [2,7,11,15]
target = 26
result = {}
pair = None

for i, n in enumerate(nums):
    diff = target - n
    if diff in result:
        pair = (result[diff], i)
    result[n] = i

if pair:
    print("Output: ", pair)
else:
    print("No pair found")