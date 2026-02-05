# Factorial of N using recursion


# Time complexity O(N)
# Space complexity O(N) - stackspace
def fact(n):
	if n==0 or n==1:
		return 1

	return n * fact(n-1)


n = 10
print(f"Factorial of {n} is {fact(n)}")