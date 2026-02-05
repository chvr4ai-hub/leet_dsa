# Given two lists n and m
# Calculate number frequency of each item from m in n list

# Constraints
# 0 <= (n[i],m[i]) <= 10
# n can have 10^8 (100 million)
# m can have 10^8 (100 million)



# time complexity O(nm)
# space complexity O(1)

# In worst case, this method may throw TLE exception since the operations are exceeding 10^8
def brute_force(n=[], m=[]):
	res = {}

	for i in range(0, len(m)):
		mval = m[i]
		for j in range(0, len(n)):
			nval = n[j]

			if mval == nval:
				res[mval] = res.get(mval, 0) + 1
			else:
				res[mval] = res.get(mval, 0) + 0


	return res

# Optimal 1: when constraint 1 is mandatory to follow: we can use hash_lst
# Time complexity O(N+M)
# Space complexity O(1) or O(11)
def optimal1(n=[], m=[]):
	hash_lst = [0]*11

	for num in n:
		if num>=0 and num<=10: # skip if any num is greater than 10 or less than 0 (constraint 1)
			hash_lst[num] += 1

	for num in m:
		if num<0 or num>10:
			print(f"Frequency of {num} is: 0")
		else:
			print(f"Frequency of {num} is: {hash_lst[num]}")



# Optimal 2: when constraint 1 is not mandatory. i.e give list can have >10 numbers. We can use dict mapping
# Time complexity O(N+M)
# Space complexity O(K), where K is the number of distinct items in the given list
def optimal2(n=[], m=[]):
	dict_map = {}

	for num in n:
		dict_map[num] = dict_map.get(num, 0) + 1

	for mnum in m:
		print(f"Frequency of {mnum} is: {dict_map.get(mnum, 0)}")


n = [1,1,1,2,2,2,4,5,1,2,6,7,8,9,67]
m = [2,4,1,9,0,4,67]

print("Brute force result: ", brute_force(n, m))

print("Optimal 1 results: ")
optimal1(n, m)

print("Optimal 2 results: ")
optimal2(n, m)














