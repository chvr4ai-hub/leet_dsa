# Find nth fibanocci number


# Time complexity O(2^N)
# Space complexity O(2^N)
def fib(n):
	tmp = []
	if n==0 or n==1:
		return n
	else:
		return fib(n-1)+fib(n-2)

n=10
print(f"find fibanocci series number for {n}: ", fib(n))

