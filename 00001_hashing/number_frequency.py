# time complexity O(N)
# space complexity O(N)
def brute_force(nums=[]):
	l = len(nums)
	num_freq = {}

	for i in range(0, l):
		n = nums[i]
		if n in num_freq:
			num_freq[n] += 1
		else:
			num_freq[n] = 1

	return num_freq


# time complexity O(N)
# space complexity O(N)
def optimal(nums=[]):
	l = len(nums)
	num_freq = {}

	for i in range(0, l):
		num_freq[nums[i]] = num_freq.get(nums[i], 0) + 1

	return num_freq


nums = [1,6,7,8,9,1,2,3,4,5,6,7,1,6,6,6]
print("Brute Force method result: ", brute_force(nums))

print("Optimal/short method result: ", optimal(nums))