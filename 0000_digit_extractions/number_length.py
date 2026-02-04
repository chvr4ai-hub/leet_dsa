# Find the length of given integer number
# time complexity O(log n) or O(log10 n) ?

n = 123454353454

# num = n
# res = 0

# while num > 0:
#     num = num // 10
#     res += 1

# print("Result: ", res)

# O(1) approach

print("Result: ", len(str(n)))

# O(1) approach using math library

import math

print("Result: ", math.floor(math.log10(n)) + 1)




