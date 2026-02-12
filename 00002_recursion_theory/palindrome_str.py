# check if given str is palindrome or not



# Time complexity is O(N)
# Space complexity is O(N)
def is_palindrome(str, l=None, r=None):
	l = l or 0
	r = r or len(str)-1
	
	if l>=r:
		return True

	
	if str[l].lower() == str[r].lower():
		is_palindrome(str, l+1, r-1)
		return True
	else:
		return False


input_str = "lirila"
res = is_palindrome(input_str)
print(f"Given string '{input_str}' is {'Palindrome' if res else 'Not a Palindrome'}")