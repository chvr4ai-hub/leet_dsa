# Find factors or divisibles of given number

import math

# time complexity O(N)
# space complexity O(K) where K is the number of factors
def bruteforce(n):
    divisibles = []
    for i in range(1, n+1):
        if n % i == 0:
            divisibles.append(i)
    
    return divisibles

# Mathematically divisibles cannot be greater than half of the given number except the number itself
# time complexity O(N/2) - Almost O(N)
# space complexity O(K)
def better(n):
    result = []
    for i in range(1, (n//2 + 1)):
        if n % i == 0:
            result.append(i)
    
    # append number itself
    result.append(n)
    return result

# mathematically divisibles are in pairs: current divisible and floor division of n by current divisible
# time complexity O(sqrt(N))+O(N log N) where N log N is for sorting
# space complexity O(K)
def optimal(n):
    result = []

    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            result.append(i)

            if n//i != i:
                result.append(n//i)
    
    result.sort()
    return result



# Examples
n = 19
result = bruteforce(n)
print("divisibles of n (Bruteforce): ", result)

n = 19
result = better(n)
print("divisibles of n (Better): ", result)

n = 19
result = optimal(n)
print("divisibles of n (Optimal): ", result)