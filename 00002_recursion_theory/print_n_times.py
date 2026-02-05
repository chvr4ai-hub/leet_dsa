# print something N times in recursive method


# Head recursion
def print_ntimes(pstr, n):
	if n==0:
		return

	print(pstr)
	print_ntimes(pstr, n-1)

# TAIL recursion
def print_ntimes_tail_recursion(pstr, n):
	if n==0:
		return

	print_ntimes_tail_recursion(pstr, n-1)
	print(pstr)

pstr = 'Hello'
n = 5

print("HEAD recursion")
print_ntimes(pstr, n)

print("TAIL recursion output:")
print_ntimes_tail_recursion(pstr, n)