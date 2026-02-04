# Find given number is armstrong number or not

# time complexity O(log10 N)
# space complexity O(1)
from math import *

n = 1534

num = n
total = 0 
nod = floor(log10(n)) + 1 # no of digits

while num > 0:
    ld = num % 10
    total = total + (ld ** nod)
    num = num // 10

if total==n:
    print("Given number is armstrong number: ", n)
else:
    print("Given number is not an armstrong number: ", n)