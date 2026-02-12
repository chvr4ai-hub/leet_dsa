# Given a list and given left, right positions, reverse the list between left and right (inclusive) using recursion.

# Time complexity O(N/2) ~= O(N)
# Space complexity O(N/2) ~= O(N)
def reverse_arr(left, right, lst=[]):
	if left>=right:
		return lst

	tmp = lst[left]
	lst[left] = lst[right]
	lst[right] = tmp
	left = left+1
	right = right-1
	reverse_arr(left, right, lst)

	return lst


left = 1
right = 5

lst = [5,6,7,2,4,1,0,9,4,5,1]
lst_original = lst.copy()


res = reverse_arr(left, right, lst)
print("Original list: ", lst_original)
print(f"Output list with {left} and {right} reversed: {res}")