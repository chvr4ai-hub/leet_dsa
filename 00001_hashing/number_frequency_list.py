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
		tmp = {}
		for j in range(0, len(n)):
			nval = n[j]

			if mval == nval:
				res[mval] = res.get(mval, 0) + 1
			else:
				res[mval] = 0


	return res


n = [1,1,1,2,2,2,4,5,1,2,6,7,8,9]
m = [2,4,1,9,0,4,67]

print("Brute force result: ", brute_force(n, m))