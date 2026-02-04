n = 123

num = n
result = 0

while num > 0:
  ld = num % 10 # last digit (reminder value of division)
  result = (result * 10) + ld
  num = num // 10 # floor division

if n == result:
    print("Given number is palindrome: ", n)
else:
    print("Given number is not a palindrome: ", n)
    