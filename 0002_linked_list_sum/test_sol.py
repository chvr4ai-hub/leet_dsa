from sol import Solution, ListNode
from typing import List, Optional

def to_linked_list(arr: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def to_list(node: Optional[ListNode]) -> List[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def test_add_two_numbers():
    sol = Solution()
    
    # Example 1
    l1 = to_linked_list([2, 4, 3])
    l2 = to_linked_list([5, 6, 4])
    result = sol.addTwoNumbers(l1, l2)
    assert to_list(result) == [7, 0, 8]
    
    # Example 2
    l1 = to_linked_list([0])
    l2 = to_linked_list([0])
    result = sol.addTwoNumbers(l1, l2)
    assert to_list(result) == [0]
    
    # Example 3
    l1 = to_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = to_linked_list([9, 9, 9, 9])
    result = sol.addTwoNumbers(l1, l2)
    assert to_list(result) == [8, 9, 9, 9, 0, 0, 0, 1]

if __name__ == "__main__":
    test_add_two_numbers()
    print("All tests passed!")
